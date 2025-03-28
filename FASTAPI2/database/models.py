from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    apellidos: str
    numero: str
    correo: str
    passw: str


class Login(BaseModel):
    correo: str
    passw: str 


class Muebles(BaseModel):
    nombre: str 


class Material(BaseModel): 
    nombre: str
    tipo: str
    price: float
    descripcion: str 
    origen: str 