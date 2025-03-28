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


class Muebles:
    nombre: str 


class Material: 
    nombre: str