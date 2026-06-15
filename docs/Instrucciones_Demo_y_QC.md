# Plataforma de Gestión del Módulo Habitar (CPU - UNSAM)
## Instrucciones de acceso a la demo y manual de testeo

**Grupo 10.** Julián Fraga, Martín Groisman, Tomás Korenblit, Marcelo Velizán.
Trabajo Práctico Final Integrador, Ingeniería de Software, 1C 2026.

---

## 1. Acceso a la demo

La demo del MVP se encuentra desplegada y disponible de forma pública en la siguiente
dirección:

> **https://habitar-cpu.onrender.com**

El entorno está alojado en un plan gratuito que suspende el servicio cuando permanece
inactivo durante un tiempo. Por ese motivo, la primera carga puede demorar entre treinta
y cincuenta segundos mientras el servicio se reactiva, y las siguientes resultan
inmediatas. Si la pantalla permanece en blanco, es suficiente con esperar unos segundos y
actualizar la página una vez. La plataforma redirige automáticamente a la pantalla de
ingreso y no requiere
ninguna instalación ni configuración por parte del evaluador.

### 1.1. Cuentas de prueba

Todas las cuentas comparten la contraseña **`habitar123`**, y cada una accede al panel que
corresponde a su rol.

| Rol | Usuario (email) | Alcance dentro de la plataforma |
|---|---|---|
| Estudiante | `ana@alumno.unsam.edu.ar` | Descubrir actividades, inscribirse, registrar asistencia y seguir su progreso |
| Coordinación (administración) | `coordinacion@unsam.edu.ar` | Gestionar actividades, inscriptos y asistencia, importar y exportar datos, ver analítica |
| Docente o facilitador | `docente@unsam.edu.ar` | Tomar la asistencia de sus actividades mediante el código de acreditación |
| Director de carrera | `director@unsam.edu.ar` | Consultar la analítica en modo de solo lectura |

La cuenta `ana@alumno.unsam.edu.ar` ya tiene actividades inscriptas, una asistencia
acreditada y créditos acumulados, de modo que las pantallas de progreso e historial
muestran datos desde el primer acceso.

### 1.2. Alta de un estudiante nuevo

El alta de estudiantes valida la matrícula contra el padrón de la UNSAM (SIU Guaraní). En
este MVP esa verificación se encuentra simulada mediante un padrón cargado en el sistema.
Para registrar una cuenta nueva desde la opción *Creá tu cuenta*, el evaluador puede
utilizar cualquiera de los legajos habilitados: 1003, 1004, 1005, 1006, 1007, 1008, 2001 o
2002. Un legajo que no figure en ese conjunto, por ejemplo el 9999, es rechazado con el
mensaje *El legajo no figura en el padrón UNSAM (SIU Guaraní)*, lo que evidencia el control
de identidad sobre el alta.

### 1.3. Datos precargados

Al iniciarse, el sistema carga de forma idempotente un conjunto de datos de
demostración que permite recorrer la plataforma sin preparación previa. Ese conjunto
incluye el padrón de legajos válidos, las cuatro cuentas de rol descritas más arriba, una
serie de actividades de ejemplo en distintos estados y fechas, las preguntas frecuentes y
el umbral de aprobación del módulo, fijado en diez créditos. Entre las actividades se
destaca el *Taller de hábitos de estudio*, que tiene un cupo de solo dos lugares para
permitir reproducir el control de cupos, y la *Bienvenida al campus*, que ya cuenta con una
asistencia acreditada.

---

## 2. Recorridos sugeridos

Los recorridos que siguen reproducen los flujos descritos en el whitepaper (sección 8.8) y
conviene ejecutarlos en el orden propuesto.

**Estudiante.** El estudiante ingresa con la cuenta `ana@alumno.unsam.edu.ar` y observa en
el inicio su barra de progreso, la sección de próximas actividades y el historial de las ya
completadas. A continuación abre el listado de actividades, aplica los filtros por tipo,
fecha, créditos y cupo, y entra al detalle de una actividad para inscribirse con un click.
Una vez en la actividad registra su asistencia ingresando el código de seis dígitos que
muestra el docente (sección 2, recorrido del docente), responde de manera opcional la
encuesta de satisfacción y regresa al inicio, donde verifica que los créditos y el progreso
se actualizaron.

**Coordinación.** La coordinación ingresa con `coordinacion@unsam.edu.ar` y parte del panel,
donde encuentra el resumen de actividades publicadas, borradores e inscripciones. Desde
allí crea una actividad nueva, la revisa con la vista previa y la publica para que sea
visible a los estudiantes. Luego abre el listado de inscriptos de una actividad, valida la
asistencia y exporta la nómina a CSV o a Excel. Por último consulta la analítica del módulo
y administra las preguntas frecuentes.

**Docente.** El docente ingresa con `docente@unsam.edu.ar`, elige una de sus actividades y
abre la pantalla de asistencia. La plataforma muestra un código QR y un código de seis
dígitos que se renueva cada noventa segundos; el estudiante lo escanea o lo ingresa en su
portal para acreditar su presencia. De manera alternativa, el docente puede marcar la
asistencia manualmente desde la lista de inscriptos.

**Director de carrera.** El director ingresa con `director@unsam.edu.ar` y accede a la
analítica en modo de solo lectura. No dispone de opciones para crear ni modificar
actividades.

---

## 3. Manual de testeo

Este manual acompaña la evaluación de la demo y describe, épica por épica, qué
comportamiento se espera observar y con qué datos reproducirlo. Su propósito es que el
evaluador pueda confirmar, sin asistencia del equipo, que cada requisito funcional y cada
atributo de calidad definido en el whitepaper se cumple en el entorno desplegado. La
organización por épicas sigue la del whitepaper (secciones 8.6 y 8.7).

**Épica 1, autenticación y perfil.** Se verifica que un estudiante con un legajo presente en
el padrón, por ejemplo el 1003, puede registrarse e ingresar correctamente, que un legajo
ausente como el 9999 es rechazado con un mensaje claro sin que se cree la cuenta, que la
coordinación accede con su usuario al backoffice y que un director de carrera ingresa a una
vista de analítica de solo lectura. El control de acceso por rol se comprueba intentando
abrir una sección de administración con una cuenta de estudiante, ante lo cual el sistema
responde con una pantalla de acceso denegado.

**Épica 2, descubrimiento y exploración.** Se verifica que el listado muestra únicamente las
actividades publicadas, que los filtros por fecha, tipo, créditos y cupo operan tanto de
forma individual como combinada, y que el detalle de cada actividad es coherente con los
datos cargados por la coordinación.

**Épica 3, inscripción y control de cupos.** Se verifica el flujo de inscripción con un click
y la recepción de la confirmación correspondiente. Como casos críticos, se comprueba que el
sistema impide inscribirse en una actividad sin cupo, que detecta y rechaza una inscripción
duplicada, y que ante dos inscripciones simultáneas por el último lugar solo una prospera.
La actividad *Taller de hábitos de estudio*, con un cupo de dos lugares, permite reproducir
ese límite.

**Épica 4, recordatorios y seguimiento.** Se verifica que la sección *Mis próximas
actividades* refleja las inscripciones vigentes del estudiante, que el recordatorio por
correo queda agendado para las veinticuatro horas previas al inicio de la actividad, y que
la sección de preguntas frecuentes muestra el contenido administrado por la coordinación.

**Épica 5, registro de asistencia.** Se prueba el flujo de acreditación presencial: la
persona a cargo de la actividad muestra un código que se renueva cada noventa segundos y el
estudiante lo ingresa desde su portal. Se verifica que un código vencido es rechazado, que
un estudiante no inscripto no puede acreditar su asistencia, y que un segundo intento de
acreditación sobre la misma actividad es bloqueado por el sistema.

**Épica 6, encuesta de satisfacción.** Se verifica que la encuesta se ofrece al estudiante
inmediatamente después de acreditar su asistencia y que la respuesta queda asociada tanto a
la actividad como al estudiante.

**Épica 7, progreso del estudiante.** Se verifica que los créditos acumulados son correctos
y coherentes con el historial de actividades completadas, y que la barra de progreso refleja
el avance real respecto del umbral de aprobación del módulo.

**Épica 8, gestión de actividades.** Se verifica el flujo completo de creación, vista previa,
publicación y edición de una actividad. Un caso particular consiste en editar una actividad
ya publicada que tiene inscriptos y comprobar que el sistema notifica el cambio a cada uno
de ellos.

**Épica 9, gestión de inscriptos y asistencia.** Se verifica que el listado de inscriptos por
actividad es correcto, que cada validación de asistencia queda registrada con su
responsable, y que la exportación a CSV y a Excel y la importación del padrón de legajos
funcionan sobre archivos válidos.

**Épica 10, analítica y reportes.** Se verifica que las métricas y los gráficos del tablero
son coherentes con los datos de la base, y que el director de carrera accede a esa
información en modo de solo lectura.

### 3.1. Criterios de aceptación

Se considera que la demo supera la evaluación cuando cada uno de los comportamientos
descritos se reproduce en el entorno desplegado y los únicos errores observados son los
previstos, es decir, los rechazos de validación y la pantalla de acceso denegado para los
roles sin permiso. Cualquier error no controlado, como una página de error inesperada, se
considera un defecto a corregir.

---

## 4. Notas técnicas y alcance del MVP

La demo está construida con FastAPI, SQLAlchemy y Jinja2 sobre una base de datos PostgreSQL
(Neon), y se despliega como una imagen Docker. Las decisiones de alcance se documentan en el
whitepaper: la verificación contra el SIU Guaraní está simulada mediante un padrón cargado;
las notificaciones se resuelven dentro de la aplicación y por correo, sin un broker
intermedio; y los gráficos se generan con Chart.js. Cuando no hay un servidor de correo
configurado, el envío de mensajes utiliza una salida de consola, de modo que los
recordatorios y las confirmaciones quedan registrados en el log del servidor en lugar de
enviarse. El código fuente, junto con el documento de diseño y este manual, se encuentra en
el repositorio del proyecto.

Quedamos a disposición para cualquier consulta durante la evaluación.
