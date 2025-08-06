# db_manager.py (versión TEXT)
import psycopg
import os
import json
import numpy as np
# import face_recog
# import get_face
# import face_recognition

DATA_BASE_URL = os.getenv("DATABASE_URL")


def np_array_to_Json(vector):
    return json.dumps(vector.tolist())


def json_to_np_array(vector_string):
    return np.array(json.loads(vector_string))

""" Agrega un usuario a la base de datos"""

def new_user(name, vector_json):
    conn = psycopg.connect(DATA_BASE_URL)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO "usuarios" (name,vector) VALUES (%s,%s)',(name, vector_json))
    conn.commit()
    conn.close()


def exist_user(vector_json):
    conn = psycopg.connect(DATA_BASE_URL)
    cursor = conn.cursor()

    vector = json_to_np_array(vector_json)
    cursor.execute('SELECT * FROM usuarios')
    row = cursor.fetchone()
    while row is not None:
        vector_db = json_to_np_array(row[2])
        exist_face = compare_vectors(vector, vector_db)
        if exist_face:
            return exist_face, row[1]
        row = cursor.fetchone()
    conn.close()
    return False, None


def compare_vectors(vec1, vec2, threshold=0.6):  # Luego colocar en un archivo utils
    dist = np.linalg.norm(vec1 - vec2)
    return dist < threshold
