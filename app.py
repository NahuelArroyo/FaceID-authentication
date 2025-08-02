import cv2
import face_recognition
import numpy as np
import os
import time

name = input("\n\n\n\nIngrese su nombre\n")
dni = input("Ingrese su DNI\n")

# 1. Abrir la webcam
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise IOError("No se pudo acceder a la cámara")

print("\n\n\nPresioná 's' para sacar la foto, la camara se abrira en 4 segundos...")
time.sleep(4)

while True:
    ret, frame = cam.read()
    cv2.imshow("Captura de rostro", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):  # 's' para sacar la foto
        cv2.imwrite(f"images/{name}_{dni}.jpg", frame)
        print(f"Foto guardada como '{name}_{dni}.jpg'")
        break

cam.release()
cv2.destroyAllWindows()

# 2. Cargar imagen y detectar rostro
image = face_recognition.load_image_file(f"images/{name}_{dni}.jpg")
face_locations = face_recognition.face_locations(image)

# Borrar archivo jpg
try:
    os.remove(f"images/{name}_{dni}.jpg")
except:
    print("Hubo un error al borrar el archivo temporal de tu rostro")

if not face_locations:
    print("\n\nNo se detectó ningún rostro.")
else:
    # 3. Extraer encoding (vector de 128 floats)
    face_encoding = face_recognition.face_encodings(
        image, known_face_locations=face_locations)[0]

    # 4. Guardar el vector
    np.save(f"vectors_faces/{name}_{dni}_encoding.npy", face_encoding)
    print(f"Vector guardado como '{name}_{dni}_encoding.npy'")
