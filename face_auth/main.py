import cv2
import get_face
import face_recog
import compare

def main():
    print("******************************Bienvenido******************************\n")
    print("\n***En caso de querer salir del programa preciona Ctrl+C o Ctrl+D***")
    try:    
        while 1:
            response_user = input("0 == Start sesion || 1 == Register :\n")
            if int(response_user) == 0:
                print("Vamos a utilizar su camara para obtener su id\n")
                get_face.get_face()
                #id_user = input("Introduci tu Usuario:")
                face_recog.get_vector(id_user)
                compare.compare_faces(id_user)
                exit(0)
            elif int(response_user) == 1:
                print("Vamos a utilizar su camara para añadir su cara a la base de datos\n")
                print("Al momento de guardar la imagen, guardarla con su nombre de usuario\n")
                id_user = input("Introduci un nombre de usuario: ")
                frame = get_face.get_face(id_user)
                is_register = face_recog.get_vector(frame,id_user)

                if is_register is None :
                    print("\nTe registraste, inicia sesion con los datos que proporcionaste\n")
                    continue
                else :
                    print(f"Ya te encontras registrado, no seas culiado {is_register}")
                    print("Inicia sesion con tu nombre de usuario mongolico (con el que te registrate la primera vez)\n")
                    continue
    except (KeyboardInterrupt, EOFError):
        print("\nSaliendo del programa")  
        exit(0)           
            
main()