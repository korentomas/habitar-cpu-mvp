# Guion de presentación, Grupo 10

Plataforma de Gestión del Módulo Habitar (CPU - UNSAM).

## Cómo usar este guion
- No es para leer palabra por palabra. Son disparadores: la idea de cada slide y cómo arrancarla.
- Hablás vos, la slide es el apoyo visual. Si te ponés a leer la slide, perdés a la platea.
- Lo que está entre comillas es una forma sugerida de decirlo, no un libreto. Decilo con tus palabras.
- Ensayalo 2 o 3 veces hasta que te salga solo.

## Reparto y tiempo (ajustar al límite que den)
| Parte | Slides | Quién | Tiempo aprox |
|---|---|---|---|
| Apertura | 1 | Marce | 30 s |
| Contexto y problema | 2-6 | Marce | 3 min |
| Propuesta de solución | 7-9 | Juli | 3 min |
| Arquitectura y riesgos | 10-11 | Martin | 3 min |
| Metodología, cronograma, conclusiones | 12-14 | Tomás | 3 min |
| Demo en vivo (cierre) | despues de la 14 | Tomás | 4 min |

Total aprox 16 min + preguntas.

---

## Apertura (Marce, slide 1)

Hook concreto, después el equipo y la hoja de ruta.

- Arrancá con el número que duele: "Cada año entran cerca de 150 estudiantes al CPU, y para
  aprobar tienen que juntar 10 horas de actividades. Hoy todo eso se lleva en papel y en
  planillas sueltas."
- "Somos el Grupo 10. Hicimos una plataforma web para reemplazar ese proceso."
- Hoja de ruta corta: "Les muestro el problema, la propuesta, la arquitectura, los riesgos,
  cómo lo planificamos, y al final una demo de la app funcionando en vivo."
- Transición: "Empecemos por cómo se gestiona hoy."

---

## Contexto y problema (Marce, slides 2-6)

**Slides 2-3, sistema actual.** Idea: hoy es todo manual y disperso.
- "El alumno busca las actividades en un documento, se anota por un Google Form distinto para
  cada una, y avisa su asistencia por otro formulario o por mail."
- Transición: "Esto trae tres problemas concretos."

**Slide 4, consultas y cupos.** Idea: la coordinación se satura y el alumno no ve nada.
- "A la coordinación le entra la misma pregunta mil veces: cuántas horas tengo, cómo acredito."
- "Y el alumno no ve los cupos: se entera de que está lleno cuando le dicen que no entra."

**Slide 5, asistencia en papel.** Idea: no escala y no hay respaldo.
- "Cada uno sube fotos de una planilla firmada, y una persona verifica las firmas una por una."
- "Si se pierde la foto, no hay backup. Son 150 por año."

**Slide 6, datos desperdigados.** Idea: los datos existen pero no se pueden usar.
- "Cada actividad tiene su propia planilla de Sheets. Sacar una estadística simple es trabajo a mano."
- Handoff: "Con esto sobre la mesa, Juli les muestra qué proponemos." (pasás a Juli)

---

## Propuesta de solución (Juli, slides 7-9)

**Slide 7, lado estudiante.** Idea: una sola plataforma central.
- "En vez de mil canales, una sola web app. El estudiante ve su progreso, busca actividades,
  se inscribe con un click y ve los cupos en tiempo real."
- (Mostrá los screenshots de la slide. La demo en vivo va al final.)

**Slide 8, lado administración.** Idea: la coordinación gestiona todo desde un lugar.
- "La coordinación carga actividades, ve quién está inscripto, exporta los listados, y tiene
  tableros con datos que antes no existían."

**Slide 9, impacto.** Idea: tres cambios concretos.
- "Menos consultas por mail, una sola vía de inscripción en lugar de mil forms, y datos para decidir."
- Handoff: "Cómo está hecha por dentro lo cuenta Martin."

---

## Arquitectura y riesgos (Martin, slides 10-11)

**Slide 10, arquitectura.** Idea: capas clásicas de web app.
- Recorré el diagrama de izquierda a derecha: "Cliente, front, back con módulos por dominio,
  y la base de datos."
- "Hay dos paneles, el del estudiante y el de la administración, pero cuatro perfiles de
  permiso: estudiante, coordinación, docente y director."
- "La identidad se verifica contra el SIU solo al darse de alta; después las credenciales
  viven en nuestra base."
- Si preguntan: tené a mano que es pub/sub para las notificaciones y lo de 2 paneles / 4 perfiles.

**Slide 11, riesgos.** Idea: identificamos 6, casi todos técnicos, y cada uno con su plan.
- No leas los 6. Contá los 2 más importantes:
- "El más fuerte es el SIU: si se cae, no podés dar de alta. Lo cubrimos con un simulador y un
  acceso de emergencia."
- "El de presencialidad, que truchen el QR, lo cubrimos con un QR que rota cada 90 segundos."
- "El resto está en la matriz, con su probabilidad e impacto."
- Handoff: "Cómo lo planificamos y en cuánto tiempo, Tomás."

---

## Metodología, cronograma y conclusiones (Tomás, slides 12-14)

**Slide 12, metodología.** Idea: Scrumban + un ciclo por sprint.
- "Trabajamos en Scrumban: sprints y tablero Kanban."
- "Dentro de cada sprint usamos un ciclo de spec-driven development: primero la especificación,
  después el plan técnico, las tareas, y recién ahí implementamos."

**Slide 13, cronograma.** Idea: lo estimamos y tiene un camino crítico claro.
- "Partimos del user story mapping, agrupamos en épicas y estimamos con Planning Poker en
  story points."
- "Los pasamos a horas con la capacidad del equipo: da unas 628 horas, repartidas en 10 sprints."
- Señalá la cadena: "Este es el camino crítico. La épica más pesada es Asistencia, que se lleva
  dos sprints, y es también la de más riesgo por el SIU y la concurrencia."
- Importante: hablá en sprints, no en semanas (1 sprint = 2 semanas).

**Slide 14, conclusiones.** Idea: a quién le sirve.
- "Le sirve a los tres: a la coordinación le baja horas de gestión, a la dirección le da datos
  para decidir, y al estudiante le da todo centralizado y un registro de asistencia con respaldo."
- Transición a la demo: "Y para cerrar, se los muestro funcionando."

---

## Demo en vivo (Tomás, cierre)

Cierre fuerte: "esto no es un mockup, está desplegado y andando".

**Antes de empezar (no saltear):**
- Calentar Render 1 o 2 min antes (el plan gratis hiberna, primer carga 30-50 s) y dejar la sesión abierta.
- Dos ventanas listas: una de estudiante, una de docente (para el QR).
- Video de backup abierto en otra pestaña por si falla el wifi.
- Cuentas (contraseña `habitar123`): ana@alumno.unsam.edu.ar, coordinacion@unsam.edu.ar, docente@unsam.edu.ar.

**Estudiante (login ana):**
- Inicio: barra de progreso 0/10 y "Mis próximas actividades".
- Actividades: filtrar por tipo, fecha, créditos, cupo. Abrir el detalle.
- Inscribirse con un click.
- Asistencia: en la otra ventana, el docente muestra el código de 6 dígitos; volvés a la del
  alumno, lo ingresás, y suma los créditos.
- Encuesta rápida y vuelta al inicio: el progreso se actualizó.

**Administración (login coordinación):**
- Panel con el resumen, crear una actividad, vista previa, publicar.
- Ver inscriptos y exportar a CSV o Excel.
- Analítica: el gráfico de inscriptos contra asistencias y la tasa de asistencia.

---

## Preguntas que pueden caer (respuestas cortas)

- *El cronograma va en semanas o en sprints?* En sprints. 1 sprint = 2 semanas, total 628 horas, está en el whitepaper.
- *Dijeron 2 perfiles pero hay 4.* Son 2 paneles (portal y backoffice) y 4 perfiles de permiso. Los 4 salen de las historias (US-04 director, US-16 docente).
- *Cómo funciona el acceso de emergencia del SIU?* El alta queda pendiente de verificación y se confirma cuando el SIU vuelve, o la coordinación la aprueba a mano mientras tanto.
- *Para qué la carga de archivos?* Para migrar e integrar los listados que hoy viven en planillas, no para validar horas.
- *Qué es el riesgo de defectos en UAT?* Que un bug grave aparezca recién en las pruebas del final y no quede tiempo de arreglarlo. Por eso desarrollamos primero lo esencial e integramos continuo.
- *Por qué pub/sub?* Para desacoplar las notificaciones: el que publica un cambio no necesita conocer a cada inscripto.

## Reglas de oro
- No leer la slide. La slide es apoyo.
- Hablar en sprints, no en semanas.
- Calentar Render antes de la demo y tener el video de backup.
- Pausas, mirar al público, no correr.
