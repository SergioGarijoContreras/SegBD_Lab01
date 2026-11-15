from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import logging, os, re, requests

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("api")

app = FastAPI(title="API NoSQL (hardened)")

# Autenticación mongo y mínimo privilegio basado en RBAC implementado init_monjo.js
mongo = MongoClient(
    host=os.getenv("MONGO_HOST", "mongo"),
    username=os.getenv("MONGO_APP_USERNAME"),
    password=os.getenv("MONGO_APP_PASSWORD"),
    authSource=os.getenv("MONGO_DATABASE", "tienda"),
)
db = mongo[os.getenv("MONGO_DATABASE", "tienda")]

class Login(BaseModel):
    username: str
    password: str

class Pedido(BaseModel):
    producto: str
    cantidad: int

@app.post("/login_mongo")
#Se define corrutina asíncrona para validación de peticiones de tipo Login
async def login(login_data: Login):
    # $eq explícito obligatoriedad de que deba usarse valor igual al consultado en login
    user = db.usuarios.find_one({
        "username": {"$eq": login_data.username},
        "password": {"$eq": login_data.password},
    }, {"_id": 0})
    if user:
        return {"msg": "ok"}
    log.warning("Login fallido: %s", login_data.username)  # Alerta por login fallido
    raise HTTPException(status_code=401, detail="Bad creds")

@app.get("/articulos")
def art_search(q: str = "", page: int = 1, size: int = 10):
    # Rechazo y alerta por uso de wildcard
    if not q or q == "*":
        log.warning("Detectada wildcard: %r", q)  # Alerta en logs
        raise HTTPException(status_code=400, detail="Consulta no permitida")

    # Consulta parametrizada
    q_seguro = re.escape(q)

    # Evitar 500 si el índice no existe
    return requests.get(
        "http://elasticsearch:9200/articulos/_search",
        params={
            "q": q_seguro,
            "from": (page - 1) * size,
            "size": size,
            "ignore_unavailable": "true",
        },
        auth=("elastic", os.getenv("ELASTIC_PASSWORD")), #Autenticación con Elasticsearch
    ).json()
