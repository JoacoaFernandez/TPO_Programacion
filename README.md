# DOCUMENTO DE ALCANCE DEL PROYECTO
## Administrador de tareas (To-Do List)

**PROGRAMACIÓN I**

---

## 1. Datos generales

| Campo | Valor |
|---|---|
| **Nombre del proyecto / sistema** | Administrador de tareas (To-Do List) |
| **Integrante 1** | Martina Fernández - Legajo: 1238681 |
| **Integrante 2** | Joaquín Fernández - Legajo: 1166347 |
| **Integrante 3** | Natalia Apostolu - Legajo: 1165678 |
| **Integrante 4** | Lucas Sambuco - Legajo: 1176135 |
| **Docente / fecha** | Lic. Julia Monasterio - 20/08/2026 |

---

## 2. Descripción general del sistema

El proyecto consiste en un administrador de tareas para grupos pequeños. La idea es que varias personas puedan organizar el trabajo desde un mismo programa, crear usuarios, formar grupos y asignar cada tarea a una persona. Cada tarea va a tener un nombre, una descripción, una prioridad, una fecha y un estado. Además, el sistema permitirá modificar algunos datos de las tareas, ver estadísticas y usar la cantidad de tareas completadas para repartir mejor las próximas asignaciones.

---

## 3. Objetivos del proyecto

**Objetivo general:** desarrollar en Python un programa que ayude a un grupo a organizar tareas y repartirlas entre sus integrantes.

**Objetivos específicos:**

- Registrar usuarios y organizarlos en grupos para poder asignar responsabilidades.
- Crear tareas con la información necesaria para saber qué hay que hacer y para cuándo.
- Permitir modificar datos de las tareas cuando cambie la situación.
- Mostrar estadísticas simples del trabajo realizado por cada usuario.
- Usar esas estadísticas para repartir nuevas tareas de una forma más equilibrada.

---

## 4. Alcance de la entrega del 40%

En esta entrega se presentará una parte funcional del sistema con la base necesaria para trabajar con usuarios, grupos y tareas. Las opciones incluidas deberán poder ejecutarse y demostrarse de principio a fin.

### 4.1 Funcionalidades incluidas

- Crear usuarios y mostrar los usuarios cargados.
- Crear grupos de trabajo y asociar usuarios a cada grupo.
- Agregar tareas indicando nombre, descripción, prioridad y fecha.
- Asignar cada tarea a un usuario del grupo.
- Mostrar las tareas con su responsable, fecha, prioridad y estado.
- Marcar una tarea como completada.
- Usar un menú básico para acceder a las opciones disponibles.
- Controlar que los datos obligatorios estén cargados correctamente.

### 4.2 Funcionalidades explícitamente NO incluidas en esta entrega

- Eliminar y buscar tareas.
- Modificar la descripción de una tarea ya cargada.
- Cambiar la prioridad de las tareas según la cercanía de su fecha.
- Mostrar estadísticas generales y por usuario.
- Aplicar un beneficio al usuario que haya completado más tareas para equilibrar la próxima distribución.

---

## 5. Alcance de la entrega del 100%

La entrega final incluirá todo lo presentado en el 40% y sumará las funciones necesarias para que el sistema permita organizar mejor el trabajo del grupo y hacer un seguimiento de lo que realiza cada usuario.

### 5.1 Funcionalidades incluidas

- Gestionar usuarios, permitiendo agregarlos, consultarlos y quitarlos.
- Crear grupos de trabajo y asociar usuarios a cada grupo.
- Crear tareas con nombre, descripción, prioridad, fecha, estado y usuario asignado.
- Mostrar, buscar, completar y eliminar tareas.
- Modificar la descripción de una tarea cuando sea necesario.
- Ordenar las tareas por prioridad y actualizar esa prioridad según la cercanía de la fecha.
- Mostrar estadísticas con la cantidad de tareas asignadas, completadas y pendientes, tanto del grupo como de cada usuario.
- Tener en cuenta las tareas completadas por cada usuario para repartir mejor las próximas tareas. La idea es que quien haya completado más pueda recibir una tarea menos o un beneficio equivalente en la siguiente distribución.
- Contar con un menú completo y validaciones básicas para evitar datos incorrectos.

### 5.2 Límites del sistema (qué queda fuera del proyecto)

- No se desarrollará una interfaz gráfica.
- No habrá inicio de sesión, contraseñas ni distintos permisos de acceso.
- No se conectará con páginas web, aplicaciones móviles, calendarios externos ni servicios de notificaciones.
- No se utilizará una base de datos.
- El programa estará pensado para usarse de forma local desde una misma ejecución.

---

## 6. Requerimientos funcionales

Los siguientes requerimientos indican qué debe poder hacer el sistema. La numeración se mantendrá durante el proyecto para poder seguir los cambios entre entregas.

| ID | Descripción del requerimiento | Criterio de aceptación | Prioridad |
|---|---|---|---|
| RF-01 | El sistema debe permitir agregar, consultar y quitar usuarios. | Un usuario agregado aparece en la lista de usuarios y uno eliminado deja de aparecer. | Alta |
| RF-02 | El sistema debe permitir crear grupos de trabajo y asociar usuarios a cada grupo. | Al consultar un grupo se pueden ver los usuarios que forman parte de él. | Alta |
| RF-03 | El sistema debe permitir asignar cada tarea a un usuario. | La tarea muestra claramente qué usuario es responsable de realizarla. | Alta |
| RF-04 | El sistema debe permitir crear una tarea ingresando nombre, descripción, prioridad y fecha. | Al finalizar la carga, la tarea aparece con todos esos datos y con estado Pendiente. | Alta |
| RF-05 | El sistema debe mostrar las tareas cargadas con su información principal. | Se visualizan el nombre, la descripción, la prioridad, la fecha, el estado y el usuario asignado. | Alta |
| RF-06 | El sistema debe permitir marcar una tarea como completada. | La tarea seleccionada cambia su estado de Pendiente a Completada. | Alta |
| RF-07 | El sistema debe permitir eliminar una tarea. | La tarea seleccionada deja de aparecer en la lista. | Media |
| RF-08 | El sistema debe permitir buscar una tarea. | Si la tarea existe se muestran sus datos y, si no existe, el programa informa que no fue encontrada. | Media |
| RF-09 | El sistema debe permitir modificar la descripción de una tarea ya cargada. | La nueva descripción reemplaza a la anterior y se muestra al consultar la tarea. | Media |
| RF-10 | El sistema debe poder actualizar la prioridad de una tarea según la cercanía de su fecha. | Al aplicar la actualización, la prioridad cambia siguiendo la regla de fechas definida para el proyecto. | Alta |
| RF-11 | El sistema debe mostrar estadísticas del trabajo realizado. | Se puede consultar cuántas tareas están asignadas, completadas y pendientes en total y por usuario. | Media |
| RF-12 | El sistema debe tener en cuenta las tareas completadas por cada usuario al repartir nuevas tareas. | El sistema identifica quién completó más tareas y permite que reciba una tarea menos o un beneficio equivalente en la siguiente distribución. | Media |
| RF-13 | El sistema debe controlar los datos ingresados en las opciones principales. | No se aceptan campos obligatorios vacíos ni valores de prioridad que estén fuera de las opciones definidas. | Alta |
| RF-14 | El sistema debe permitir salir del programa desde el menú. | Al elegir la opción Salir, el programa finaliza correctamente. | Alta |

---

## 7. Requerimientos no funcionales

- **Usabilidad:** el menú y los mensajes deben ser simples y fáciles de entender.
- **Compatibilidad:** el programa debe ejecutarse con Python y sin depender de herramientas externas no autorizadas para la materia.
- **Claridad:** el código debe estar organizado en funciones con nombres que indiquen qué hace cada una.

---

## 8. Supuestos y riesgos

### 8.1 Supuestos

- Cada usuario tendrá un nombre que permita identificarlo dentro del grupo.
- Cada tarea quedará asignada a un usuario a la vez.
- Las fechas se ingresarán usando un mismo formato definido para todo el programa.
- Las estadísticas se calcularán con las tareas registradas en el sistema.
- El trabajo se realizará de manera grupal y las partes desarrolladas se integrarán en un único programa.

### 8.2 Riesgos identificados

- Que al unir las partes hechas por distintos integrantes aparezcan errores de integración.
- Que la relación entre usuarios, grupos y tareas necesite ajustes durante el desarrollo.
- Que la regla para cambiar prioridades según las fechas necesite modificarse después de probarla.
- Que haya empates entre usuarios al comparar quién completó más tareas y sea necesario definir cómo aplicar el beneficio.
- Que alguna funcionalidad lleve más tiempo del previsto y sea necesario reorganizar las tareas del grupo.

---

## 9. Observaciones

- La implementación se realizará con los contenidos y herramientas de Python trabajados en clase o autorizados por la docente.
- La regla exacta para modificar prioridades según las fechas se definirá antes de programar esa parte, manteniendo la idea de dar más importancia a las tareas que estén más cerca de vencer.
- El beneficio por cumplimiento podrá ser una tarea menos en la siguiente distribución o una alternativa similar que sirva para equilibrar el trabajo del grupo.
- Si durante el desarrollo se modifica alguna funcionalidad o criterio de aceptación, el cambio se dejará aclarado en una versión posterior de este documento.