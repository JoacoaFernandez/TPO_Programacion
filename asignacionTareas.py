###USUARIOS
 
def crear_usuario(nombre_usuario, grupo=None):
    usuario = {
        "nombre_usuario": nombre_usuario,
        "grupo": grupo,
        "tareas_completadas": 0
    }
    return usuario
 
usuarios = []
 
def agregar_usuario(lista_usuarios, nombre_usuario, grupo=None):
    nuevo = crear_usuario(nombre_usuario, grupo)
    lista_usuarios.append(nuevo)
    return nuevo
 
def mostrar_usuarios(lista_usuarios):
    if not lista_usuarios:
        print("No hay usuarios cargados.")
        return
    for u in lista_usuarios:
        print("Nombre:", u["nombre_usuario"], "- Grupo:", u["grupo"], "- Tareas completadas:", u["tareas_completadas"])
 
def buscar_usuario(lista_usuarios, nombre_usuario):
    for u in lista_usuarios:
        if u["nombre_usuario"] == nombre_usuario:
            return u
    return None
 
 
###GRUPOS
 
def agregar_grupo(lista_grupos, nombre_grupo):
    if nombre_grupo in lista_grupos:
        return None
    lista_grupos.append(nombre_grupo)
    return nombre_grupo
 
def mostrar_grupos(lista_grupos, lista_usuarios):
    if not lista_grupos:
        print("No hay grupos cargados")
        return
 
    for grupo in lista_grupos:
        
        integrantes = [u["nombre_usuario"] for u in lista_usuarios if u["grupo"] == grupo]
        print("Grupo:", grupo, "- Integrantes:", len(integrantes))
 
def buscar_grupo(lista_grupos, nombre_grupo):
    for grupo in lista_grupos:
        if grupo.lower() == nombre_grupo.lower():
            return grupo
    return None
 
def asociar_usuario_a_grupo(lista_usuarios, lista_grupos, nombre_usuario, nombre_grupo):
    
    usuario = buscar_usuario(lista_usuarios, nombre_usuario)
    grupo = buscar_grupo(lista_grupos, nombre_grupo)
 
    if usuario is None or grupo is None:
        return False
 
    usuario["grupo"] = grupo
    return True

###TAREAS

def crear_tarea(idTarea, nombre_grupo_tarea, descripcion, prioridad, fecha, grupo, responsable):
    
    tarea = {
        "id": idTarea,                  
        "nombre_grupo_tarea": nombre_grupo_tarea,
        "descripcion": descripcion,
        "prioridad": prioridad,         
        "fecha": fecha,                 
        "estado": "Pendiente",          
        "grupo": grupo,                 
        "responsable": responsable      
    }
    return tarea


def agregar_tarea(lista_tareas, nombre_grupo_tarea, descripcion, prioridad, fecha, grupo, responsable):
    idTarea = len(lista_tareas) + 1    
    nueva = crear_tarea(idTarea, nombre_grupo_tarea, descripcion, prioridad, fecha, grupo, responsable)
    lista_tareas.append(nueva)         
    return nueva


def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas cargadas.")
        return

    for t in lista_tareas:     
        print("ID:", t["id"], "-", t["nombre_grupo_tarea"])
        print("  Descripción:", t["descripcion"])
        print("  Grupo:", t["grupo"], "- Responsable:", t["responsable"])
        print("  Fecha:", t["fecha"], "- Prioridad:", t["prioridad"], "- Estado:", t["estado"])
        print()     


def buscar_tarea_por_id(lista_tareas, idTarea):
    for t in lista_tareas:         
        if t["id"] == idTarea:     
            return t               
    return None                    


def marcar_tarea_completada(lista_tareas, lista_usuarios, idTarea):
    tarea = buscar_tarea_por_id(lista_tareas, idTarea)     

    if tarea is None:                      
        return False                       
    if tarea["estado"] == "Completada":    
        return False                       

    tarea["estado"] = "Completada"         

   
    responsable = buscar_usuario(lista_usuarios, tarea["responsable"])
    if responsable is not None:
        responsable["tareas_completadas"] += 1     

    return True     