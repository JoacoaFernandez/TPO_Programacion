###USUARIOS

def crear_usuario(nombre, grupo=None):
    usuario = {
        "nombre": nombre,
        "grupo": grupo,
        "tareas_completadas": 0
    }
    return usuario

usuarios = []

def agregar_usuario(lista_usuarios, nombre, grupo=None):
    nuevo = crear_usuario(nombre, grupo)
    lista_usuarios.append(nuevo)
    return nuevo

def mostrar_usuarios(lista_usuarios):
    if not lista_usuarios:
        print("No hay usuarios cargados.")
        return
    for u in lista_usuarios:
        print("Nombre:", u["nombre"], "- Grupo:", u["grupo"], "- Tareas completadas:", u["tareas_completadas"])

def buscar_usuario(lista_usuarios, nombre):
    for u in lista_usuarios:
        if u["nombre"] == nombre:
            return u
    return None


###GRUPOS

def agregar_grupo(lista_grupos, nombre):
    if nombre in lista_grupos:
        return None
    lista_grupos.append(nombre)
    return nombre

def mostrar_grupos(lista_grupos,lista_usuarios):
    if not lista_grupos:
        print("No hay grupos cargados")
        return

    for grupo in lista_grupos:
        integrantes = [u["Nombre"] for u in lista_usuarios if u["grupo"] == grupo]
        print("Grupo:", grupo, "- Integrantes:", len(integrantes))

def buscar_grupo(lista_grupos, nombre):
    for grupo in lista_grupos:
        if grupo.lower() == nombre.lower():
            return grupo
    return None

def asociar_usuario_a_grupo(lista_usuarios, lista_grupos, nombreUsuario, nombreGrupo):
    usuario = buscar_usuario(lista_usuarios, nombreUsuario)
    grupo = buscar_grupo(lista_grupos, nombreGrupo)

    if usuario is None or grupo is None:
        return False

    usuario["grupo"] = grupo
    return True


