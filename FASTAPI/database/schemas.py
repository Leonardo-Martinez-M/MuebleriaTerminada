def individual_users(usuario):
    return {
        "id": str(usuario["_id"]),
        "nombre": str(usuario["nombre"]),
        "apellidos": str(usuario["apellidos"]),
        "numero": str(usuario["numero"]),
        "correo": str(usuario["correo"]),
        "passw": str(usuario["passw"])
    }

def all_users(usuarios):
    return [individual_users(usuario) for usuario in usuarios]
