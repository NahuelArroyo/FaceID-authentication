import os
import json
import face_recognition
import numpy as np

"""
En este archivo vamos a comparar los vectores embebidos 
segun la distancia entre ellos para detectar rostros  cuando
dos rostros son distintos o son el mismo
"""
def compare_faces(id_user):
    try:
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ids")
        id_json = id_user + ".json"
        user_path = os.path.join(directory, id_json)
        """
        Creamos el vector embebido del usuario ingresado
        """
        if not os.path.exists(user_path):
            print("No se encontró la información del usuario en la base de datos")
            return
        with open(user_path, "r") as f:
            data_user = json.load(f)
        vector_user = np.array(data_user[0]["embedding"])

        json_list = get_name_json()
        """
        Comparamos el vector del usuario con los ya registrados 
        """
        found_match = False
        for j in json_list:
            if j == id_json:
                continue
            
            path_j = os.path.join(directory, j)
            with open(path_j, "r") as f:
                data_db = json.load(f)
            
            vector_db = np.array(data_db[0]["embedding"])

            result = face_recognition.compare_faces([vector_db], vector_user)
            #print(f"Comparando con {j} -> {result[0]}")
            
            if result[0]:
                found_match = True
                print("\nAcceso aceptado: Bienvenido al sistema ", j)
                break
        
        if not found_match:
            print("No se encontró coincidencia en la base de datos")
    
    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))
        
          
def get_name_json():
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ids")
    files = os.listdir(directory)
    
    names_of_files = []
    for f in files:
        if f.endswith(".json"):
            names_of_files.append(f)
    return names_of_files


