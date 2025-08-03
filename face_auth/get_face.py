import cv2
import time
import face_recog

"""Abrimos la webcam (0 es decir, la default) para obtener la cara 
de la persona y asi luego poder compararla con la base de datos"""

def get_face():

    # 1. Abrir la webcam
    cam = cv2.VideoCapture(0)
    
    if not cam.isOpened():
        raise IOError("No se pudo acceder a la cámara")
    
    # Setear resolución 1080p
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    time.sleep(2)

    window_name = "Captura de rostro - Presiona 's' para capturar"

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)  # permite redimensionar
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # pantalla completa
    cv2.resizeWindow(window_name, 1920, 1080)  # forzar tamaño 1080p

    while True:
        ret, frame = cam.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            break

    cam.release()
    cv2.destroyAllWindows()
    
    if not ret:
        print("No se pudo capturar el frame\n")
        return None
    
    return frame
