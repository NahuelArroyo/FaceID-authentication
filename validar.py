import numpy as np
from face_recognition import compare_faces, face_distance

v1 = np.load("vectors_faces/Nahuel_46509352_encoding.npy")
v2 = np.load("vectors_faces/Nahuel2_20_encoding.npy")

result = compare_faces([v1], v2)[0]
distancia = face_distance([v1], v2)[0]

print("¿Son la misma persona?:", result)
print("Distancia entre vectores:", distancia)
