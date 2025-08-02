import cv2
import time

"""Abrimos la webcam (0 es decir, la default) para obtener la cara 
de la persona y asi luego poder compararla con la base de datos"""

def get_face(id_user=None):

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
            print(f"Foto guardada como '{id_user}.jpg'")
            break

    cam.release()
    cv2.destroyAllWindows()
    
    return frame

