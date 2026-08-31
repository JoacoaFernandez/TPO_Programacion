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