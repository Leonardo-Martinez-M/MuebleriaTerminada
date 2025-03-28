from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from configrations import collection
from database.schemas import all_users 
from database.models import Usuario
from database.models import Login
from database.schemas import individual_users

app = FastAPI()
router= APIRouter()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite solicitudes desde localhost:3000 (tu frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

@router.post("/login")
async def login(login_data: Login):
    user= collection.find_one({"correo": login_data.correo})

    if user is None:
        raise HTTPException(status_code=404, detail="Usuario noo encontrado")
    
    if user["passw"] != login_data.passw:
        raise HTTPException(status_code=401, detail="Contraseña Inconrrecta")
    
    user_data = individual_users(user)
    return {"message": "Inicio de sesion exitoso", "user": user_data}


@router.get("/get_all_users")
async def get_all_users():
    data = collection.find()
    return all_users(data)


@router.post("/create")
async def create_users(new_user: Usuario):
    try:
        resp = collection.insert_one(dict(new_user))
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e :
        return HTTPException(status_code=500, detail=f"Ocurrio algun error. {e}")
    

app.include_router(router)
