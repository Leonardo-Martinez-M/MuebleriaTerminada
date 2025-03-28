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


def individual_material(material):
    return {
        "id": str(material["_id"]),
        "nombre": str(material["nombre"]),
        "tipo": str(material["tipo"]),
        "price": str(material["price"]),
        "descripcion": str(material["descripcion"]),
        "origen": str(material["origen"])
    }

def all_materiales(materiales):
    return [individual_material(material) for material in materiales]