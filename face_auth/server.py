from fastapi import FastAPI, Request
import requests
import os
import conn_db
import sqlite3

app = FastAPI()


@app.post("/procesar-vector")
async def proc_vector(request: Request):
    data = await request.json()
    vector_json = data.get("vector")
    val, name = conn_db.exist_user(vector_json)
    return {"Exist": bool(val), "Name": name}


@app.post("/register")
async def register(request: Request):
    data = await request.json()
    vector = data.get("vector")
    name = data.get("name")
    conn_db.new_user(name, vector)
    return {"message": f"Usuario '{name}' registrado correctamente "}
