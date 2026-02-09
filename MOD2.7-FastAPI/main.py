from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo"}

@app.get("/usuarios")
def obtener_usuarios():
    return [{"nombre":"pokemon molon"}, "Luis", "María"]

@app.post("/usuarios")
def crear_usuario():
    return {"status": "Usuario creado"}
