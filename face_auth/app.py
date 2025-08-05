import requests
import json
import face_recognition
import conn_db, face_recog, get_face


def main():
    #print("******************************Bienvenido******************************\n")
    print("\n***En caso de querer salir del programa preciona Ctrl+C o Ctrl+D***")

    try:    
        while 1:
            response_user = input("\n0==Iniciar sesion o 1==Registrarse\n")
            if int(response_user) == 0:
                print("Vamos a utilizar su camara para obtener su id\n")
                vector = face_recog.get_vector(get_face.get_face())

                vector_string = conn_db.np_array_to_Json(vector)
                url = "http://127.0.0.1:8000/procesar-vector"
                payload = {"vector": vector_string}
                response = requests.post(url,json=payload)
                
                """Respuesta del servidor al cliente"""
                val = response.json().get("Exist")
                Name = response.json().get("Name")
                
                if val:
                    print(f"Bienvenido {Name}, que gusto verte de nuevo :)!!")
                    exit(0)
                else:
                    print(f"Perdon!! No te pudimos encontrar prueba registrandote")

            elif int(response_user) == 1:
                print("Vamos a utilizar su camara para obtener su id\n")
                vector = face_recog.get_vector(get_face.get_face())

                vector_string = conn_db.np_array_to_Json(vector)
                url = "http://127.0.0.1:8000/procesar-vector"
                payload = {"vector": vector_string}
                response = requests.post(url,json=payload)
                
                """Respuesta del servidor al cliente"""
                val = response.json().get("Exist")
                Name = response.json().get("Name")
                
                if val:
                    print(f"Que haces {Name}!!!, anda a iniciar sesion :)!!")
                    exit(0)
                else:
                    name = input("Introduci un nombre de usuario: ")
                    
                    url = "http://127.0.0.1:8000/register"
                    payload.update({"name": name}) 
                    response = requests.post(url,json=payload)
                    message = response.json().get("message")

                    print(message)
    except (KeyboardInterrupt, EOFError):
        print("\nSaliendo del programa")  
        exit(0)           
            
main()

    
    
    
    




    
    

