# Plataforma de Gestión del Módulo Habitar (CPU - UNSAM)
## Instrucciones de Acceso a la Demo y Manual de Testeo / QC

**Grupo 10**, Julián Fraga, Martín Groisman, Tomás Korenblit, Marcelo Velizán
Trabajo Práctico Final Integrador, Ingeniería de Software, 1C 2026

---

## 1. Acceso a la demo

La demo del MVP se encuentra desplegada y disponible públicamente en:

> **https://habitar-cpu.onrender.com**

**Nota sobre el primer acceso:** el entorno está alojado en un plan gratuito que
hiberna el servicio tras un período de inactividad. La primera carga puede demorar
**entre 30 y 50 segundos** mientras el servicio se reactiva; las siguientes son
inmediatas. Si la pantalla queda en blanco, basta con esperar y refrescar una vez.

La plataforma redirige automáticamente a la pantalla de ingreso. No requiere
instalación ni configuración por parte del evaluador.

### 1.1. Cuentas de prueba (precargadas)

Todas las cuentas usan la contraseña **`habitar123`**.

| Rol | Usuario (email) | Qué puede hacer |
|---|---|---|
| Estudiante | `ana@alumno.unsam.edu.ar` | Descubrir actividades, inscribirse, registrar asistencia, ver progreso |
| Coordinación (administración) | `coordinacion@unsam.edu.ar` | Gestionar actividades, inscriptos, asistencia, importar/exportar, analítica |
| Docente / facilitador | `docente@unsam.edu.ar` | Tomar asistencia de sus actividades (código QR) |
| Director de carrera | `director@unsam.edu.ar` | Consultar la analítica (solo lectura) |

> La cuenta `ana@alumno.unsam.edu.ar` ya tiene actividades inscriptas, una asistencia
> acreditada y créditos acumulados, de modo que las pantallas de progreso e historial
> muestran datos desde el primer momento.

### 1.2. Alta de un estudiante nuevo (verificación SIU simulada)

El alta de estudiantes valida la matrícula contra el padrón de la UNSAM (SIU Guaraní).
En el MVP esa verificación está **simulada** con un padrón cargado. Para registrar una
cuenta nueva desde *“Creá tu cuenta”*, utilice uno de los siguientes legajos válidos:

> **1003, 1004, 1005, 1006, 1007, 1008, 2001, 2002**

Un legajo fuera de ese conjunto (por ejemplo `9999`) es rechazado con el mensaje
*“El legajo no figura en el padrón UNSAM (SIU Guaraní)”*, demostrando el control de identidad.

### 1.3. Datos precargados

El sistema inicializa, de forma idempotente, un conjunto de datos de demostración:

- Padrón de legajos válidos y las cuatro cuentas de rol descritas arriba.
- Actividades de ejemplo en distintos estados y fechas:
  - *Bienvenida al campus* (presencial, pasada, 2 créditos), con asistencia ya acreditada.
  - *Taller de hábitos de estudio* (presencial, dentro de 24 h, 3 créditos, **cupo 2** para evidenciar el control de cupos).
  - *Charla: vida universitaria* (virtual, 2 créditos).
  - *Laboratorio abierto de Física* (presencial, 4 créditos).
  - *Taller de escritura* en estado **borrador** (no visible para estudiantes).
- Preguntas frecuentes y el umbral de aprobación del módulo (**10 créditos**).

---

## 2. Recorridos sugeridos (camino feliz)

Los siguientes recorridos reproducen los flujos descritos en el whitepaper
(sección 8.8). Se recomienda ejecutarlos en este orden.

### 2.1. Estudiante (autoservicio)
1. Ingresar con `ana@alumno.unsam.edu.ar`.
2. En **Inicio** observar la barra de progreso, *“Mis próximas actividades”* y el historial.
3. Ir a **Actividades**, aplicar filtros (tipo, fecha, créditos, con cupo) y abrir el detalle de una actividad.
4. Presionar **Inscribirme**: el sistema confirma la inscripción y genera una notificación.
5. Ir a **Registrar asistencia** (ver sección 2.3 para obtener el código del docente),
   ingresar el código de 6 dígitos y validar.
6. Completar (opcionalmente) la **encuesta** de satisfacción.
7. Volver a **Inicio** y verificar que los créditos y el progreso se actualizaron.

### 2.2. Coordinación (backoffice)
1. Ingresar con `coordinacion@unsam.edu.ar`.
2. En el **Panel** revisar el resumen en tarjetas (publicadas, borradores, inscripciones).
3. **+ Nueva actividad** → completar datos → **Guardar** (queda en borrador) → **Vista previa** → **Publicar**.
4. **Inscriptos** → seleccionar una actividad → revisar la lista, validar asistencia y **exportar a CSV / Excel**.
5. **Inscriptos → Importar padrón de legajos**: subir un archivo `.csv`/`.xlsx` con la columna `legajo`.
6. **Analítica** → revisar métricas y gráficos de cohorte.
7. **FAQ** → administrar las preguntas frecuentes.

### 2.3. Docente (acreditación de asistencia)
1. Ingresar con `docente@unsam.edu.ar`.
2. En **Mis actividades** elegir una y presionar **Tomar asistencia**.
3. Se muestra un **código QR rotativo + un código de 6 dígitos** (se renueva cada 90 segundos).
4. El estudiante escanea el QR o ingresa el código en su portal (sección 2.1, paso 5).
5. Alternativamente, el docente puede marcar la asistencia manualmente desde la lista de inscriptos.

### 2.4. Director de carrera
1. Ingresar con `director@unsam.edu.ar`.
2. Acceder a **Analítica** (solo lectura). El director no puede crear ni modificar actividades.

---

## 3. Manual de Testeo / QC

Casos de prueba de aceptación organizados por épica (alineados con las secciones 8.6
y 8.7 del whitepaper). Cada caso indica **precondición → pasos → resultado esperado**.

### E-01. Autenticación y perfil
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-01 | Login válido | Ingresar con una cuenta de prueba | Acceso al panel correspondiente al rol |
| T-02 | Login inválido | Contraseña incorrecta | Mensaje *“Email o contraseña incorrectos”* |
| T-03 | Alta con legajo válido | Registrarse con legajo 1003 | Cuenta creada e ingreso automático |
| T-04 | Alta con legajo inválido | Registrarse con legajo 9999 | Rechazo: *“no figura en el padrón UNSAM”* |
| T-05 | Control de acceso por rol | Como estudiante, abrir `/admin` | Pantalla **403 - Sin permiso** |

### E-02. Descubrimiento y exploración
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-06 | Listado | Abrir **Actividades** | Se ven solo las actividades publicadas |
| T-07 | Filtros | Filtrar por tipo / fecha / créditos / con cupo | El listado se reduce según el criterio |
| T-08 | Detalle | Abrir una actividad | Se ven datos completos y el cupo disponible |

### E-03. Inscripción y control de cupos
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-09 | Inscripción | Inscribirse en una actividad con cupo | Confirmación + notificación por mail/in-app |
| T-10 | Baja | Darse de baja | Se libera el cupo |
| T-11 | Cupo lleno | Inscribir un 3.er estudiante en *“Taller de hábitos de estudio”* (cupo 2) | Rechazo: *“No quedan cupos disponibles”* |

### E-04. Recordatorios y seguimiento
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-12 | Próximas actividades | Inicio del estudiante | Sección *“Mis próximas actividades”* poblada |
| T-13 | FAQ | Abrir **Ayuda** | Se ven las preguntas frecuentes |
| T-14 | Recordatorio 24 h | (Automático) | El sistema agenda el envío 24 h antes del inicio |

### E-05. Registro de asistencia con QR
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-15 | Acreditación | Docente abre asistencia → estudiante ingresa el código | *“¡Asistencia registrada!”* + suma de créditos |
| T-16 | Código vencido | Ingresar un código viejo (> 90 s) | Rechazo: *“El código expiró”* |
| T-17 | No inscripto | Acreditar a un estudiante no inscripto | Rechazo: *“No estás inscripto en esta actividad”* |
| T-18 | Doble acreditación | Validar dos veces | Rechazo: *“Tu asistencia ya fue registrada”* |

### E-06. Encuesta de satisfacción
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-19 | Encuesta | Tras acreditar, responder la encuesta | Respuesta guardada y asociada a la actividad |

### E-07. Progreso del estudiante
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-20 | Créditos y barra | Inicio del estudiante | Créditos acumulados y barra de progreso correctos |
| T-21 | Historial | Inicio del estudiante | Listado de actividades completadas |

### E-08. Gestión de actividades (administración)
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-22 | Alta | Crear una actividad | Queda en estado borrador |
| T-23 | Vista previa | Vista previa antes de publicar | Se ve como la verá el estudiante |
| T-24 | Publicación | Publicar | La actividad pasa a ser visible para estudiantes |
| T-25 | Edición + aviso | Editar una actividad publicada con inscriptos | Se notifica automáticamente a los inscriptos |

### E-09. Inscriptos y asistencia (administración)
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-26 | Listado de inscriptos | Abrir **Inscriptos** de una actividad | Lista con estado de asistencia |
| T-27 | Exportación | Exportar a CSV y a Excel | Se descargan los archivos con los inscriptos |
| T-28 | Importación | Importar un CSV/XLSX con columna `legajo` | Se incorporan los legajos nuevos al padrón |

### E-10. Analítica y reportes
| ID | Caso | Pasos | Resultado esperado |
|---|---|---|---|
| T-29 | Dashboard | Abrir **Analítica** (coordinación o director) | Tarjetas + gráficos (inscriptos vs. asistencias, más elegidas) y promedios de encuesta |
| T-30 | Solo lectura | Como director, intentar gestionar actividades | No tiene acceso a la edición |

### 3.1. Criterios de aceptación
Se considera la prueba **superada** cuando todos los casos T-01 a T-30 arrojan el
resultado esperado, sin errores no controlados (pantallas 403/500 solo en los casos previstos).

---

## 4. Notas técnicas y alcance del MVP

- **Stack:** FastAPI + SQLAlchemy + Jinja2 sobre PostgreSQL (Neon), desplegado con Docker.
- **Decisiones del MVP** (documentadas en el whitepaper): la verificación SIU Guaraní está
  simulada con un padrón cargado; las notificaciones se resuelven in-app + mail (sin broker
  Redis); los gráficos se renderizan con Chart.js; el envío de mails usa una *backend de consola*
  si no hay SMTP configurado (los recordatorios y confirmaciones se registran en el log del servidor).
- **Código fuente:** el repositorio incluye el `README.md`, el documento de diseño y este manual.

Quedamos a disposición para cualquier consulta durante la evaluación.
