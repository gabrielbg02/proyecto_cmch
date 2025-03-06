from fastapi import FastAPI, Request, Form, staticfiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pydantic import BaseModel
import os

app = FastAPI()
app.mount("/static", staticfiles.StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


MONGODB_URI = "mongodb://localhost:27017/" 
client = MongoClient(MONGODB_URI)

try:
    client.admin.command('ping')
    print("Conexión a MongoDB exitosa")
except ConnectionFailure:
    print("No se pudo conectar a MongoDB")

db = client.contraloria
formulario = db.formulario

class datos_formulario(BaseModel):
    nombre: str
    correo: str
    cargo: str
    numero_cedula: str
    numero_telefono_jefe: str
    estado: str
    municipio: str
    nombre_organismo: str
    instancia: str
    cantidad_denuncias: str
    cantidad_reclamos: str
    cantidad_quejas: str
    cantidad_peticiones: str
    cantidad_sugerencias: str
    cantidad_asesorias: str
    cantidad_poblacion_masc: str
    cantidad_poblacion_fem: str
    cantidad_talleres_oipp: str
    cantidad_charlas_oipp: str
    cantidad_conversatorios_oipp: str
    cantidad_jornadas_oipp: str
    cantidad_forochats_oipp: str
    cantidad_adulto_masculino_atentido_oipp: str
    cantidad_adulto_femenino_atentida_oipp: str
    nombre_escuela_se: str
    cantidad_actividades_se: str
    cantidad_talleres_se: str
    cantidad_charlas_se: str
    cantidad_conversatorios_se: str
    cantidad_jornadas_se: str
    cantidad_forochats_se: str
    cantidad_ninosyadol_masculino_se: str
    cantidad_ninasyadol_femenino_se: str
    cantidad_adultos_masculino_atendidos_se: str
    cantidad_adultos_femenino_atendidos_se: str
    nombre_ministerio_ap: str
    cantidad_actividades_ap: str
    cantidad_talleres_ap: str
    cantidad_charlas_ap: str
    cantidad_jornadas_ap: str
    cantidad_forochats_ap: str
    cantidad_funcionarios_masculino_ap: str
    cantidad_funcionarios_femenino_ap: str

# Ruta para mostrar el formulario
@app.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

# Ruta para procesar el formulario
@app.post("/data-processing")
async def procesar_formulario(request: Request, datos: datos_formulario):
    datos_guardar = datos.dict()  # Obtener los datos como un diccionario
    formulario.insert_one(datos_guardar)
    return templates.TemplateResponse("exito.html", {"request": request})