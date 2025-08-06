import cv2
import time
import face_recog

"""Abrimos la webcam (0 es decir, la default) para obtener la cara 
de la persona y asi luego poder compararla con la base de datos"""


def get_face():

    # 1. Abrir la webcam
    cam = cv2.VideoCapture(0, cv2.CAP_V4L2)

    if not cam.isOpened():
        raise IOError("No se pudo acceder a la cámara")

    time.sleep(2)

    window_name = "Presioná 's' para sacar la foto, o 'q' para salir"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)  # ventana redimensionable
    cv2.resizeWindow(window_name, 800, 600)  # tamaño más cómodo
    cv2.moveWindow(window_name, 500, 200)

    while True:
        ret, frame = cam.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            break
        elif key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    if not ret:
        print("No se pudo capturar el frame\n")
        return None

    return frame
