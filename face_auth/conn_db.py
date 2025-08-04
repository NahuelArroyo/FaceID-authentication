# db_manager.py (versión TEXT)
import sqlite3
import os
import json
import numpy as np
import face_recog
import get_face

DB_PATH = os.path.join("face_auth", "data_base.db")

def crear_tabla():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        embedding TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def guardar_usuario(nombre, embedding):
    """Guarda el usuario serializando el embedding como JSON (TEXT)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    embedding_str = json.dumps(embedding.tolist())  # numpy → lista → JSON
    cursor.execute("INSERT OR REPLACE INTO usuarios (nombre, embedding) VALUES (?, ?)", (nombre, embedding_str))
    conn.commit()
    conn.close()
    print(f"✅ Usuario '{nombre}' guardado en la base (TEXT)")

def obtener_todos_los_usuarios():
    """Devuelve [(nombre, numpy.array), ...] de todos los usuarios."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, embedding FROM usuarios")
    filas = cursor.fetchall()
    conn.close()

    usuarios = []
    for nombre, emb_str in filas:
        emb = np.array(json.loads(emb_str))  # JSON → lista → numpy.array
        usuarios.append((nombre, emb))
    return usuarios

# 🔹 Crear tabla al importar
v_embedding = face_recog.get_vector(get_face.get_face())
crear_tabla()
guardar_usuario("fidelCuloRoto",v_embedding)
print(obtener_todos_los_usuarios())