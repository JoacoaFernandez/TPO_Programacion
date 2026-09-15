def crear_usuario(nombre, grupo=None):
    usuario = {
        "nombre": nombre,
        "grupo": grupo,
        "tareas_completadas": 0
    }
    return usuario


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
    return next(filter(lambda u: u["nombre"].lower() == nombre.lower(), lista_usuarios), None)


def agregar_grupo(lista_grupos, nombre):
    existe = next(filter(lambda g: g.lower() == nombre.lower(), lista_grupos), None)
    if existe is not None:
        return None
    lista_grupos.append(nombre)
    return nombre


def mostrar_grupos(lista_grupos, lista_usuarios):
    if not lista_grupos:
        print("No hay grupos cargados.")
        return
    for grupo in lista_grupos:
        integrantes = list(map(lambda u: u["nombre"], filter(lambda u: u["grupo"] == grupo, lista_usuarios)))
        print("Grupo:", grupo, "- Integrantes:", len(integrantes), "-", integrantes)


def buscar_grupo(lista_grupos, nombre):
    return next(filter(lambda g: g.lower() == nombre.lower(), lista_grupos), None)


def asociar_usuario_a_grupo(lista_usuarios, lista_grupos, nombreUsuario, nombreGrupo):
    usuario = buscar_usuario(lista_usuarios, nombreUsuario)
    grupo = buscar_grupo(lista_grupos, nombreGrupo)
    if usuario is None or grupo is None:
        return False
    usuario["grupo"] = grupo
    return True


def crear_tarea(idTarea, nombre, descripcion, prioridad, fecha, grupo, responsable):
    tarea = {
        "id": idTarea,
        "nombre": nombre,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "fecha": fecha,
        "estado": "Pendiente",
        "grupo": grupo,
        "responsable": responsable
    }
    return tarea


def agregar_tarea(lista_tareas, nombre, descripcion, prioridad, fecha, grupo, responsable):
    idTarea = len(lista_tareas) + 1
    nueva = crear_tarea(idTarea, nombre, descripcion, prioridad, fecha, grupo, responsable)
    lista_tareas.append(nueva)
    return nueva


def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas cargadas.")
        return
    for t in lista_tareas:
        print("ID:", t["id"], "-", t["nombre"])
        print("  Descripción:", t["descripcion"])
        print("  Grupo:", t["grupo"], "- Responsable:", t["responsable"])
        print("  Fecha:", t["fecha"], "- Prioridad:", t["prioridad"], "- Estado:", t["estado"])
        print()


def buscar_tarea_por_id(lista_tareas, idTarea):
    return next(filter(lambda t: t["id"] == idTarea, lista_tareas), None)


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


def pedir_texto_no_vacio(mensaje):
    valor = input(mensaje).strip()
    while valor == "":
        print("Este dato no puede estar vacío.")
        valor = input(mensaje).strip()
    return valor


def pedir_prioridad():
    prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ").strip().capitalize()
    while prioridad not in ("Alta", "Media", "Baja"):
        print("Prioridad inválida. Debe ser Alta, Media o Baja.")
        prioridad = input("Ingrese la prioridad (Alta/Media/Baja): ").strip().capitalize()
    return prioridad


def pedir_fecha():
    fecha = input("Ingrese la fecha de la tarea (dd/mm/aaaa): ").strip()
    partes = fecha.split("/")
    while len(partes) != 3 or not all(parte.isdigit() for parte in partes):
        print("Formato de fecha inválido, debe ser dd/mm/aaaa.")
        fecha = input("Ingrese la fecha de la tarea (dd/mm/aaaa): ").strip()
        partes = fecha.split("/")
    return fecha


def interfaz_agregar_usuario(lista_usuarios):
    nombre = pedir_texto_no_vacio("Ingrese el nombre del usuario: ")
    if buscar_usuario(lista_usuarios, nombre) is not None:
        print("Ya existe un usuario con ese nombre.")
        return
    agregar_usuario(lista_usuarios, nombre)
    print(f"Usuario '{nombre}' creado correctamente.")


def interfaz_agregar_grupo(lista_grupos):
    nombre = pedir_texto_no_vacio("Ingrese el nombre del grupo: ")
    if agregar_grupo(lista_grupos, nombre) is None:
        print("Ya existe un grupo con ese nombre.")
    else:
        print(f"Grupo '{nombre}' creado correctamente.")


def interfaz_asociar_usuario_a_grupo(lista_usuarios, lista_grupos):
    if not lista_usuarios:
        print("No hay usuarios cargados. Cree un usuario primero.")
        return
    if not lista_grupos:
        print("No hay grupos cargados. Cree un grupo primero.")
        return
    mostrar_usuarios(lista_usuarios)
    nombreUsuario = pedir_texto_no_vacio("Ingrese el nombre del usuario: ")
    while buscar_usuario(lista_usuarios, nombreUsuario) is None:
        print("Ese usuario no existe.")
        nombreUsuario = pedir_texto_no_vacio("Ingrese el nombre del usuario: ")
    mostrar_grupos(lista_grupos, lista_usuarios)
    nombreGrupo = pedir_texto_no_vacio("Ingrese el nombre del grupo: ")
    while buscar_grupo(lista_grupos, nombreGrupo) is None:
        print("Ese grupo no existe.")
        nombreGrupo = pedir_texto_no_vacio("Ingrese el nombre del grupo: ")
    asociar_usuario_a_grupo(lista_usuarios, lista_grupos, nombreUsuario, nombreGrupo)
    print(f"Usuario '{nombreUsuario}' asociado al grupo '{nombreGrupo}'.")


def interfaz_agregar_tarea(lista_tareas, lista_grupos, lista_usuarios):
    if not lista_grupos:
        print("No hay grupos cargados. Cree un grupo primero.")
        return
    nombre = pedir_texto_no_vacio("Ingrese el nombre de la tarea: ")
    descripcion = pedir_texto_no_vacio("Ingrese la descripción de la tarea: ")
    prioridad = pedir_prioridad()
    fecha = pedir_fecha()
    mostrar_grupos(lista_grupos, lista_usuarios)
    nombreGrupo = pedir_texto_no_vacio("Ingrese el grupo al que pertenece la tarea: ")
    grupo_real = buscar_grupo(lista_grupos, nombreGrupo)
    while grupo_real is None:
        print("Ese grupo no existe.")
        nombreGrupo = pedir_texto_no_vacio("Ingrese el grupo al que pertenece la tarea: ")
        grupo_real = buscar_grupo(lista_grupos, nombreGrupo)
    integrantes = list(filter(lambda u: u["grupo"] == grupo_real, lista_usuarios))
    if not integrantes:
        print("Ese grupo no tiene usuarios asociados. No se puede asignar la tarea.")
        return
    print(f"Usuarios del grupo '{grupo_real}':")
    for u in integrantes:
        print("-", u["nombre"])
    nombreResponsable = pedir_texto_no_vacio("Ingrese el nombre del responsable de la tarea: ")
    while buscar_usuario(integrantes, nombreResponsable) is None:
        print("Ese usuario no pertenece al grupo seleccionado.")
        nombreResponsable = pedir_texto_no_vacio("Ingrese el nombre del responsable de la tarea: ")
    responsable_real = buscar_usuario(integrantes, nombreResponsable)["nombre"]
    agregar_tarea(lista_tareas, nombre, descripcion, prioridad, fecha, grupo_real, responsable_real)
    print(f"Tarea '{nombre}' creada y asignada a {responsable_real}.")


def interfaz_marcar_tarea_completada(lista_tareas, lista_usuarios):
    if not lista_tareas:
        print("No hay tareas cargadas.")
        return
    mostrar_tareas(lista_tareas)
    idIngresado = input("Ingrese el ID de la tarea a marcar como completada: ").strip()
    while not idIngresado.isdigit():
        print("Debe ingresar un número válido.")
        idIngresado = input("Ingrese el ID de la tarea a marcar como completada: ").strip()
    exito = marcar_tarea_completada(lista_tareas, lista_usuarios, int(idIngresado))
    if exito:
        print("Tarea marcada como completada.")
    else:
        print("No se pudo completar la tarea (no existe o ya estaba completada).")


def mostrar_menu():
    print()
    print("========== ADMINISTRADOR DE TAREAS ==========")
    print("1. Crear usuario")
    print("2. Mostrar usuarios")
    print("3. Crear grupo")
    print("4. Asociar usuario a un grupo")
    print("5. Mostrar grupos")
    print("6. Agregar tarea")
    print("7. Mostrar tareas")
    print("8. Marcar tarea como completada")
    print("0. Salir")
    print("==============================================")


def salir():
    print("Saliendo del programa...")


def opcion_invalida():
    print("Opción inválida.")


def main():
    usuarios = []
    grupos = []
    tareas = []
    opciones = {
        1: lambda: interfaz_agregar_usuario(usuarios),
        2: lambda: mostrar_usuarios(usuarios),
        3: lambda: interfaz_agregar_grupo(grupos),
        4: lambda: interfaz_asociar_usuario_a_grupo(usuarios, grupos),
        5: lambda: mostrar_grupos(grupos, usuarios),
        6: lambda: interfaz_agregar_tarea(tareas, grupos, usuarios),
        7: lambda: mostrar_tareas(tareas),
        8: lambda: interfaz_marcar_tarea_completada(tareas, usuarios),
        0: salir,
    }
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcionIngresada = input("Seleccione una opción: ").strip()
        while not opcionIngresada.isdigit():
            print("Debe ingresar un número.")
            opcionIngresada = input("Seleccione una opción: ").strip()
        opcion = int(opcionIngresada)
        funcion = opciones.get(opcion, opcion_invalida)
        funcion()


main()