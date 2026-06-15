# Plataforma de Gestión del Módulo Habitar (CPU - UNSAM)
## Instrucciones de acceso a la demo y plan de pruebas

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
ingreso y no requiere ninguna instalación ni configuración por parte del evaluador.

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
2002. Un legajo que no figure en ese conjunto, por ejemplo el 9999, es rechazado con un
mensaje de error, lo que evidencia el control de identidad sobre el alta.

### 1.3. Datos precargados

Al iniciarse, el sistema carga de forma idempotente un conjunto de datos de demostración
que permite recorrer la plataforma sin preparación previa. Ese conjunto incluye el padrón
de legajos válidos, las cuatro cuentas de rol descritas más arriba, una serie de
actividades de ejemplo en distintos estados y fechas, las preguntas frecuentes y el umbral
de aprobación del módulo, fijado en diez créditos. Entre las actividades se destaca el
*Taller de hábitos de estudio*, que tiene un cupo de solo dos lugares para permitir
reproducir el control de cupos, y la *Bienvenida al campus*, que ya cuenta con una
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
muestra el docente, responde de manera opcional la encuesta de satisfacción y regresa al
inicio, donde verifica que los créditos y el progreso se actualizaron.

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

## 3. Plan de pruebas de la demo

Este plan adapta el plan de pruebas del whitepaper (sección 8.6) al entorno desplegado.
Conserva su organización por épicas y, para cada una, enuncia primero el comportamiento que
se espera observar y luego ofrece una tabla de casos concretos que el evaluador puede
reproducir y verificar por su cuenta.

### 3.1. Objetivo

El plan tiene como propósito verificar que la demo cumple los requisitos funcionales, los
atributos de calidad y los criterios de aceptación definidos en el whitepaper. La
verificación se realiza ejecutando, sobre el entorno desplegado, los casos descritos más
abajo y contrastando el resultado obtenido con el resultado esperado.

### 3.2. Alcance y tipos de prueba

Sobre la demo se ejecutan las pruebas funcionales de aceptación de cada historia de
usuario, junto con las pruebas de seguridad de control de acceso por rol y la prueba de
fiabilidad del control de cupo, que el whitepaper plantea para el escenario de dos
inscripciones simultáneas por el último lugar. Las
pruebas unitarias y de integración acompañan al código durante el desarrollo y no forman
parte de este recorrido manual. La organización de los casos sigue la del plan
de pruebas del whitepaper (sección 8.6).

### 3.3. Casos de prueba por épica

**Épica 1, autenticación y perfil.** Se verifica que el alta de estudiantes respeta el padrón
del SIU, que el ingreso distingue credenciales válidas de inválidas y que cada rol queda
confinado a las secciones que le corresponden.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Alta válida | Registrarse con el legajo 1003 y un email no utilizado antes | La cuenta se crea y el ingreso es automático |
| Alta inválida | Registrarse con el legajo 9999 | El alta se rechaza con un mensaje de error y la cuenta no se crea |
| Ingreso inválido | Ingresar con una contraseña incorrecta | Se informa que el email o la contraseña son incorrectos |
| Control de acceso | Como estudiante, abrir una sección de administración | Se muestra la pantalla de acceso denegado |
| Rol de solo lectura | Ingresar como director de carrera | Solo se ofrece la analítica, sin opciones de gestión |

**Épica 2, descubrimiento y exploración.** Se verifica que el catálogo expone únicamente las
actividades publicadas, que los filtros operan de forma individual y combinada, y que el
detalle es coherente con los datos cargados.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Listado | Abrir la sección Actividades | Se listan solo las actividades publicadas |
| Filtros | Filtrar por fecha, tipo, créditos y cupo, de forma individual y combinada | El listado se restringe según cada criterio |
| Detalle | Abrir una actividad del listado | Se muestran sus datos completos y el cupo disponible |

**Épica 3, inscripción y control de cupos.** Se verifica el flujo de inscripción con un click,
la confirmación correspondiente y el comportamiento ante los casos críticos de cupo y
duplicación.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Inscripción | Inscribirse en una actividad con cupo disponible | Se confirma la inscripción y se genera la notificación |
| Cupo completo | Inscribir estudiantes en *Taller de hábitos de estudio* hasta agotar su cupo de dos lugares e intentar una inscripción más | La inscripción que excede el cupo se rechaza por falta de cupo |
| Inscripción duplicada | Intentar inscribirse dos veces en la misma actividad | El sistema detecta el duplicado y lo rechaza |
| Baja | Darse de baja de una actividad | Se libera el cupo y se informa la baja |

**Épica 4, recordatorios y seguimiento.** Se verifica que el estudiante tiene a la vista sus
compromisos próximos, que el recordatorio por correo se genera mediante un proceso periódico
y que las preguntas frecuentes muestran el contenido de la coordinación. Por tratarse de un
proceso en segundo plano, el recordatorio no es una acción inmediata de la inscripción.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Próximas actividades | Abrir el inicio del estudiante | La sección *Mis próximas actividades* lista las inscripciones vigentes |
| Recordatorio | Un proceso en segundo plano revisa de forma periódica las actividades por comenzar | Cuando una actividad comienza dentro de las próximas 24 horas y el inscripto todavía no fue avisado, se genera el recordatorio por correo; si no hay un servidor de correo configurado, queda registrado en el log del servidor |
| Preguntas frecuentes | Abrir la sección Ayuda | Se muestran las preguntas frecuentes administradas por la coordinación |

**Épica 5, registro de asistencia.** Se prueba la acreditación presencial mediante el código
que muestra el docente y los rechazos previstos ante un código vencido, un estudiante no
inscripto o una segunda acreditación. Para reproducir estos casos con un solo dispositivo,
conviene ingresar primero como docente para obtener el código y luego como el estudiante
inscripto para acreditar la asistencia.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Acreditación | El docente abre la asistencia y el estudiante ingresa el código de seis dígitos | Se registra la asistencia y se suman los créditos de la actividad |
| Código vencido | Ingresar un código de más de noventa segundos de antigüedad, sin refrescar la pantalla del docente | La acreditación se rechaza porque el código ya no es válido |
| Estudiante no inscripto | Acreditar con una cuenta no inscripta en la actividad | La acreditación se rechaza por falta de inscripción |
| Doble acreditación | Acreditar dos veces la misma actividad | El segundo intento se rechaza por asistencia ya registrada |

**Épica 6, encuesta de satisfacción.** Se verifica que la encuesta se ofrece al estudiante
inmediatamente después de acreditar su asistencia y que la respuesta queda correctamente
asociada.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Encuesta | Responder la encuesta tras acreditar la asistencia | La respuesta se guarda asociada a la actividad y al estudiante |

**Épica 7, progreso del estudiante.** Se verifica que los créditos y el historial son
coherentes entre sí y que la barra de progreso refleja el avance respecto del umbral de
aprobación.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Créditos e historial | Abrir el inicio del estudiante | Los créditos acumulados coinciden con las actividades del historial |
| Barra de progreso | Observar la barra en el inicio | El avance se muestra respecto del umbral de diez créditos del módulo |

**Épica 8, gestión de actividades.** Se verifica el ciclo completo de creación, vista previa,
publicación y edición, incluida la notificación a los inscriptos cuando se modifica una
actividad ya publicada.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Alta | Crear una actividad nueva | La actividad queda en estado borrador |
| Vista previa | Usar la vista previa antes de publicar | Se muestra tal como la verá el estudiante |
| Publicación | Publicar la actividad | La actividad pasa a ser visible para los estudiantes |
| Edición con aviso | Editar una actividad ya publicada que tiene inscriptos | Se notifica el cambio a cada uno de los inscriptos |

**Épica 9, gestión de inscriptos y asistencia.** Se verifica que la nómina por actividad es
correcta, que cada validación queda registrada con su responsable y que la exportación e
importación de datos funcionan sobre archivos válidos.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Nómina | Abrir los inscriptos de una actividad | Se ve la nómina con el estado de asistencia de cada estudiante |
| Validación | Validar la asistencia de un inscripto desde la administración | La asistencia queda registrada con su responsable |
| Exportación | Exportar la nómina a CSV y a Excel | Se descargan los archivos con los inscriptos |
| Importación | Importar un archivo con una columna `legajo` | Se incorporan al padrón los legajos nuevos del archivo |

**Épica 10, analítica y reportes.** Se verifica que las métricas y los gráficos del tablero
son coherentes con los datos de la base y que el director accede a esa información en modo de
solo lectura.

| Caso | Cómo reproducirlo | Resultado esperado |
|---|---|---|
| Tablero | Abrir la analítica como coordinación o dirección | Las tarjetas y los gráficos coinciden con los datos de la base |
| Solo lectura | Como director, buscar opciones de gestión | No hay acceso a la edición de actividades |

### 3.4. Criterios de aceptación

Se considera que la demo supera la evaluación cuando, para cada caso de la sección 3.3, el
resultado obtenido coincide con el resultado esperado. Los únicos errores admisibles son los
previstos por el propio plan, es decir, los rechazos de validación y la pantalla de acceso
denegado para los roles sin permiso. Cualquier error no controlado, como una página de error
inesperada, se considera un defecto que debe corregirse antes de dar la prueba por aprobada.

---

## 4. Notas técnicas y alcance del MVP

La demo está construida con FastAPI, SQLAlchemy y Jinja2 sobre una base de datos PostgreSQL
(Neon), y se despliega como una imagen Docker. Las decisiones de alcance se documentan en el
whitepaper: la verificación contra el SIU Guaraní está simulada mediante un padrón cargado;
las notificaciones se resuelven dentro de la aplicación y por correo, sin un broker
intermedio; y los gráficos se generan con Chart.js. Cuando no hay un servidor de correo
configurado, el envío de mensajes utiliza una salida de consola, de modo que los
recordatorios y las confirmaciones quedan registrados en el log del servidor en lugar de
enviarse. El código fuente, junto con el documento de diseño y este plan de pruebas, se
encuentra en el repositorio del proyecto.

Quedamos a disposición para cualquier consulta durante la evaluación.
