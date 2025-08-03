import os
import face_recognition
import json

"""Realizamos el escaneo de las imagenes para obtener un json con informacion
de la persona mas un vector embebido el cual es unico"""


def get_vector(frame, id_user=None):
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Convertimos la imagen de BGR a RGB
        image = frame[:, :, ::-1].copy()

        """Pasamos imagen del frame como un objeto para utilizarlo con face_recognition"""
        face_location = face_recognition.face_locations(image)
        
        if not face_location:
            print("No se detecto ningun rostro en la captura")
            return None

        """Utilizamos la imagen en el objeto para encondearlo como un vector embebido"""
        face_encoding = face_recognition.face_encodings(image, face_location)
        
        if not face_encoding:
            print("No se pudo codificar correctamente el vector de su rostro :(")
            return None

        return face_encoding[0]

    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))
