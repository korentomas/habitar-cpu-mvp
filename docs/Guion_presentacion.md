# Guion de la presentación, Grupo 10

**Plataforma de Gestión del Módulo Habitar (CPU - UNSAM).**

Bullets para tener a la vista mientras se presenta (no leer textual). 14 slides, 4 segmentos
y la demo en vivo.

| Segmento | Slides | Presenta |
|---|---|---|
| Contexto y problema | 1-6 | Marce |
| Propuesta de solución + demo | 7-9 | Juli (narra) + Tomás (demo en vivo) |
| Arquitectura y riesgos | 10-11 | Martin |
| Metodología, cronograma y conclusiones | 12-14 | Tomás |

---

## Segmento 1, contexto y problema (1-6), Marce

**Slide 1, título**
- Plataforma de Gestión del Módulo Habitar, Grupo 10.
- En una línea: el Módulo Habitar es la materia de ingreso del CPU donde los ingresantes
  hacen actividades presenciales y virtuales para sumar 10 créditos antes de empezar la carrera.

**Slides 2-3, sistema actual**
- Hoy se gestiona con foro del campus + Google Forms + planillas de papel.
- El alumno busca actividades en un documento, se anota por formularios distintos, confirma por mail.
- La info queda desperdigada en múltiples canales.

**Slide 4, problemas (consultas y cupos)**
- Consultas repetidas por mail y foro (cuántas horas, cómo acreditar, estado de inscripción).
- Cupos no visibles: el alumno no sabe si quedan lugares hasta que le dicen "completo".

**Slide 5, problemas (papel)**
- Alrededor de 150 ingresantes por año.
- Cada uno sube fotos de su planilla firmada; una persona verifica las firmas una por una.
- Lento, artesanal y sin respaldo: si se pierde la foto, no hay backup.

**Slide 6, problemas (sheets)**
- Cada actividad tiene su planilla de Sheets; la info queda dispersa en muchos archivos.
- Consolidar para sacar estadísticas es trabajo manual. Datos que ya existen, desaprovechados.

**Cierre del segmento:** proceso manual que crece con cada camada, sin backup ni datos
explotables. Eso motiva la solución.

---

## Segmento 2, propuesta de solución + demo (7-9), Juli narra + Tomás demo

**Slide 7, web app (estudiantes), Juli**
- Una web app central para estudiantes y coordinación.
- Para el estudiante: tablero de avisos, FAQs, progreso personal, calendario, búsqueda de
  actividades, visibilidad de cupos y créditos otorgados.
- (Acá arranca la demo en vivo, parte estudiante.)

**Slide 8, web app (administración), Juli**
- Para la administración: ABM de actividades, edición de FAQs, envío de avisos, ver
  inscriptos, tableros de analítica.
- (Demo en vivo, parte admin.)

**Slide 9, impacto esperado, Juli**
- FAQs bajan las consultas repetitivas por mail.
- Inscripción central reemplaza la multiplicidad de Google Forms.
- Dashboards aportan valor sobre datos que hoy no se explotan.
- Calendario personal facilita la cursada y descongestiona consultas.

### Demo en vivo, Tomás (guion click a click)

**Antes de empezar (clave):**
- Calentar Render 1-2 min antes (el plan free hiberna, primer load 30-50s) y dejar la sesión logueada.
- Tener 2 ventanas abiertas: una de estudiante, una de docente (para el QR).
- Video de backup abierto en otra pestaña por si falla el wifi o Render.
- Cuentas (pw `habitar123`): ana@alumno.unsam.edu.ar, coordinacion@unsam.edu.ar, docente@unsam.edu.ar.

**Parte estudiante (login ana):**
- Inicio: barra de progreso 0/10 créditos y sección "Mis próximas actividades".
- Actividades: aplicar filtros (tipo, fecha, créditos, con cupo). Abrir el detalle de una.
- Inscribirse con un click, mostrar la confirmación.
- Registrar asistencia: pasar a la ventana del docente, mostrar el código de 6 dígitos que rota
  cada 90s; volver a la ventana del estudiante, ingresar el código, "asistencia registrada, sumaste créditos".
- Completar la encuesta de satisfacción.
- Volver al inicio: el progreso y los créditos se actualizaron.

**Parte admin (login coordinación):**
- Panel: resumen en tarjetas (publicadas, borradores, inscripciones).
- Crear una actividad, usar la vista previa, publicarla.
- Ver inscriptos y exportar la nómina a CSV o Excel.
- Analítica: gráficos de inscriptos vs asistencias, actividades más elegidas, tasa de asistencia.

**Cierre de la demo:** todo esto está desplegado y funcionando, no es un mockup.

---

## Segmento 3, arquitectura y riesgos (10-11), Martin

**Slide 10, arquitectura**
- Capas jerárquicas clásicas (es una web app): cliente, servidor web, backend (módulos de
  dominio), base de datos.
- 2 paneles (portal del estudiante y backoffice) pero 4 perfiles de permiso (estudiante,
  coordinación, docente, director): servicios compartidos, distintos permisos por rol.
- Estilo distribuido pub/sub para las notificaciones (cada actividad es un topic, la
  inscripción suscribe al alumno).
- Single event processing: cada acción del usuario (ej. inscribirse) es una cadena de
  eventos únicos encadenados.
- Una DB interna + consulta al SIU Guaraní solo para verificar la matrícula al alta (no SSO).
- Heads-up por si preguntan: tener a mano "2 paneles, 4 perfiles" y el pub/sub.

**Slide 11, riesgos**
- Matriz probabilidad por impacto: 6 riesgos, 5 significativos y 1 moderado.
- SIU (significativo): mitigar con un simulador + acceso de emergencia.
- Archivos corruptos en la importación (significativo): validadores estrictos + rollback transaccional.
- QR truchado / falla de presencialidad (significativo): QR rotativo con expiración + geoloc o
  wifi UNSAM + registro manual de contingencia.
- Defectos críticos tardíos en UAT (significativo): MVP-first + integración continua para que
  no aparezcan recién al final.
- Dashboard no útil para directivos (moderado, observar): validar mockups con los directivos
  antes de programar. Es el único "observar", no "mitigar".
- Incompatibilidad de capas (significativo): integrar de a piezas chicas, no dejar el ensamblado para el final.

---

## Segmento 4, metodología, cronograma y conclusiones (12-14), Tomás

**Slide 12, metodología**
- Scrumban: Scrum (sprints, revisiones, reuniones) + Kanban (flujo visual, control de WIP).
- En cada sprint, ciclo Spec-Driven Development (SDD): Specify, Plan, Tasks, Implement.
- (Opcional: el agente de código implementa en un loop con verificación humana del 100% de lo
  que entra a main.)

**Slide 13, cronograma**
- Proceso: US Mapping, agrupar en épicas, Planning Poker para estimar story points.
- Conversión de SP a horas con fundamento: 80 hs por sprint (4 personas x 10 hs/sem x 2 sem) /
  ~20 SP por sprint = 4 hs por SP. Total ≈ 628 hs.
- Camino crítico (cadena de mayor duración, define la duración mínima): Setup, Auth, CRUD
  actividades, Descubrimiento, Inscripción, Asistencia, Progreso, Hardening.
- E5 Asistencia es la épica dominante (ocupa 2 sprints) y la de mayor riesgo (SIU +
  concurrencia), por eso lleva reserva de contingencia.
- Holgura: las épicas fuera del camino crítico (recordatorios, encuesta, analítica) se
  solapan sin mover el go-live.
- Unidad correcta: SPRINTS (1 sprint = 2 semanas), no semanas. 10 sprints = 20 semanas.

**Slide 14, conclusiones**
- Beneficios en tres sectores: coordinación (menos horas de gestión y consultas), dirección
  (decisiones basadas en evidencia), estudiantes (info centralizada, cupos visibles,
  recordatorios y asistencia con respaldo digital y trazable).
- Cierre fuerte: el MVP está desplegado y funcionando, lo acaban de ver en la demo.

---

## Recordatorios para todos
- Cronograma: hablar en sprints, no en semanas (1 sprint = 2 semanas, total 628 hs en el whitepaper).
- Arquitectura: si preguntan por perfiles, son 2 paneles y 4 roles.
- Demo: calentar Render antes y tener el video de backup.
