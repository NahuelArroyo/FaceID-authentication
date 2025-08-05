# db_manager.py (versión TEXT)
import sqlite3
import os
import json
import numpy as np
import face_recog
import get_face
import face_recognition

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

conn = sqlite3.connect(f"{BASE_DIR}/data_base.db")
cursor = conn.cursor()


def np_array_to_Json(vector):
    return json.dumps(vector.tolist())


def json_to_np_array(vector_string):
    return np.array(json.loads(vector_string))


def exist_table(name_table):
    cursor.execute(
        """ SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = "table" AND name = "{}"  """.format(name_table))
    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False


""" Agrega un usuario a la base de datos"""


def new_user(name, vector):
    vector_json_string = np_array_to_Json(vector)
    cursor.execute("""INSERT INTO "usuarios" (name,vector) VALUES ("{}","{}")""".format(
        name, vector_json_string))
    conn.commit()
    conn.close()


def exist_user(vector):
    vector_json_string = np_array_to_Json(vector)
    cursor.execute("""SELECT * FROM "usuarios" """)
    row = cursor.fetchone()
    while row is not None:
        vector_db = json_to_np_array(row[2])
        exist_face = face_recognition.compare_faces([vector], vector_db)[0]
        if exist_face:
            return exist_face,row[1]
        row = cursor.fetchone()
    return False, None


val, name = exist_user(face_recog.get_vector(get_face.get_face()))

if val:
    print(f"Hola queridoo, bienvenido {name}")
else:
    print("Disculpa! No te conocemos, te invitamos a Registrarte")
