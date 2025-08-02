import os
import face_recognition
import json

"""Realizamos el escaneo de las imagenes para obtener un json con informacion
de la persona mas un vector embebido el cual es unico"""


def get_vector(frame, id_user=None):
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        image = face_recognition.load_image_file(frame)

        """Guardamos la imagen del frame como un objeto para utilizarlo con face_recognition"""
        face_location = face_recognition.face_locations(image)

        """Utilizamos la imagen en el objeto para encondearlo como un vector embebido"""
        face_encoding = face_recognition.face_encodings(image, face_location)

        """Verificamos que en la imagen el modelo pudo identificar un rostro"""
        if not face_location:
            print("\n\nNo se detectó ningún rostro.")

        """" Leer archivo JSON existente o iniciar una lista vacía """
        try:
            database_path = os.path(BASE_DIR, "ids", "database.json")
            with open(database_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            # Crear el archivo
            os.open("database.json", "w")
            data = []

        for info in data:
            for element in info:
                vector_db = element["embedding"]
                result = face_recognition.compare_faces([vector_db], face_encoding)
                if result[0]:
                    return element["name"]
        
        data.append({
                "name": id_user,
                "embedding": face_encoding
            })
        return None

    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))


"""Obtenemos un array con los vectores embebidos de los usuarios ya registrados"""


def get_info_vectors_json(data):
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ids")
    embeddings = []
    json_path = os.path.join(directory, filename)
    with open(json_path, "r") as f:
        data_vector = json.load(f)
        for entry in data_vector:
            embedding = entry.get("embedding")
            if embedding is not None:
                embeddings.append(embedding)
    return embeddings



        # # refactorizar
        # arr_embedding_vectors = get_info_vectors_json(data)

        # if face_encoding in arr_embedding_vectors:
        #     return True
        # else:
        #     data.append({
        #         "name": id_user,
        #         "embedding": face_encoding
        #     })
        #     return "Mensaje"

        # for random_vector in arr_embedding_vectors:
        #     if random_vector is face_encoding:
        #         return random_vector.(buscar indexar para saber el i)
        #     else:
        

        # json_path = os.path.join(BASE_DIR, "ids", f"{id_user}.json")
        # with open(json_path, "w") as json_end:
        # sjson.dump(data, json_end, indent=4)
    