# Cronograma y camino crítico, explicado

**Grupo 10.** Plataforma de Gestión del Módulo Habitar (CPU - UNSAM).

Este documento explica en palabras el cronograma de la sección 8.9 del whitepaper (la
diapositiva del cronograma): qué es el camino crítico, por qué la épica 5 ocupa dos
sprints, qué significa la holgura y para qué están las reservas. La escala es relativa
(sprints S0 a S9, sin fechas calendario) y la duración de cada tarea se expresa en story
points (SP) del Planning Poker, con una velocidad estimada de unos 20 SP por sprint.

---

## 1. Qué es el camino crítico

El camino crítico es la cadena de épicas que dependen una de otra y que, sumadas, dan la
duración mínima del proyecto. Cada épica de esta cadena no puede empezar hasta que la
anterior entregue lo que necesita, así que un atraso en cualquiera de ellas atrasa el
go-live. Las épicas que quedan fuera de esta cadena se pueden hacer en paralelo y tienen
margen para moverse.

La duración de cada épica está definida: son los story points del Planning Poker. El
camino crítico es, entonces, la cadena de dependencias cuya suma de SP es la más larga.

### Dependencias entre épicas

| Épica | SP | Depende de | Motivo |
|---|---|---|---|
| E1 Autenticación y perfil | 14 | Setup | El login y el control de acceso son la base de todo |
| E8 Gestión de actividades (admin) | 12 | E1 | La coordinación necesita loguearse para cargar el catálogo |
| E2 Descubrimiento | 26 | E8 | El estudiante descubre lo que la coordinación publicó |
| E3 Inscripción | 9 | E2 | Se inscribe desde el detalle y el cupo de la actividad |
| **E5 Registro de asistencia** | **31** | E3, E8 | Se acredita asistencia sobre una inscripción a una actividad |
| E7 Progreso del estudiante | 8 | E5 | Los créditos se suman después de validar la asistencia |
| E9 Inscriptos y asistencia (admin) | 10 | E3 | Hace falta que existan inscriptos |
| E4 Recordatorios | 8 | E3 | Solo recuerda inscripciones confirmadas |
| E6 Encuesta | 10 | E5 | Aparece después de confirmar la asistencia |
| E10 Analítica | 18 | E5, E9, E6 | Consume datos de asistencia, inscriptos y encuestas |

### El camino crítico de este proyecto

```
Setup → E1 (14) → E8 (12) → E2 (26) → E3 (9) → E5 (31) → E7 (8) → Hardening / Go-live
```

La suma del camino crítico es de unos 100 SP. La épica dominante es **E5 (asistencia)**:
con 31 SP es la más grande y la de mayor riesgo (integra el SIU y exige persistencia
transaccional bajo concurrencia), por eso lleva una reserva de contingencia.

---

## 2. Por qué la épica 5 ocupa dos sprints (no son dos alternativas)

En la diapositiva, E5 aparece en dos celdas, en S5 y en S6. **No son dos caminos
alternativos: es una sola épica partida en dos mitades**, porque con 31 SP no entra en un
único sprint (la velocidad es de unos 20 SP por sprint).

- **E5 parte 1 (S5), 26 SP:** US16 (el docente escanea el QR del estudiante) y US17
  (bloqueo de la acreditación remota por geolocalización o red UNSAM). Es el núcleo del
  registro de asistencia.
- **E5 parte 2 (S6), 5 SP:** US18 (override manual de la coordinación para casos
  excepcionales).

Las dos partes son secuenciales y ambas están en el camino crítico. La "parte 2" no es una
alternativa a la "parte 1": es lo que queda de la misma épica una vez que no entró en el
primer sprint. Después de E5 parte 2 viene la reserva de contingencia y el hito H4
(asistencia validada).

---

## 3. Qué es la holgura (y dónde está esa "semana" de margen)

La holgura, o margen, es cuánto puede atrasarse una épica que NO está en el camino crítico
sin mover la fecha de go-live. Una épica con holgura se puede correr a un sprint posterior,
o solapar con otra, sin afectar el hito final.

Las épicas con holgura en este cronograma son **E9 (inscriptos admin), E4 (recordatorios),
E6 (encuesta) y E10 (analítica)**. No están en la cadena crítica, así que tienen margen:

- **E9** se desarrolla alrededor de S4 y S5, pero su único consumidor aguas abajo es E10,
  que recién ocurre en S8. Por eso E9 tiene varios sprints de holgura: podría atrasarse sin
  frenar nada del camino crítico.
- **E4 y E6** están planificadas en S7. El camino crítico, en cambio, va de E5 a E7 y de
  ahí a Hardening, sin pasar por E4 ni E6. Esto les da alrededor de un sprint de holgura:
  podrían moverse hacia S8 (junto con E10) sin mover el go-live. Ese margen de un sprint es
  la "holgura de una semana".

En resumen: la holgura no es tiempo muerto ni una ruta paralela del camino crítico. Es la
flexibilidad que tienen las épicas secundarias para reordenarse mientras el camino crítico
avanza.

---

## 4. Cronograma sprint por sprint

| Sprint | Qué se hace | SP | En camino crítico | Hito al cierre |
|---|---|---|---|---|
| S0 | Setup y diseño: repo, CI/CD, modelo de datos, PoC del SIU, mockups, validación | n/a | Sí | H0 Kick-off |
| S1 | E1 Autenticación y perfil (US01-04): login SIU, perfil mínimo, roles, control de acceso | 14 | Sí | H1 Autenticación operativa |
| S2 | E8 Gestión de actividades (US24-27) + FAQ (US15): catálogo publicable | 15 | Sí | H2 Backoffice MVP |
| S3 | E2 Descubrimiento parte 1 (US05-06): calendario y filtros | 16 | Sí | (sin hito) |
| S4 | E2 Descubrimiento parte 2 (US07-08) + E3 Inscripción (US09-12). En paralelo, E9 US28 (holgura) | 19 | Sí | H3 Portal estudiante MVP |
| S5 | E5 Asistencia parte 1 (US16-17). En paralelo, E9 US29 (holgura) | 26 | Sí | (sin hito) |
| S6 | E5 Asistencia parte 2 (US18) + reserva de contingencia + E7 Progreso (US21-23) | 13 | Sí | H4 Asistencia validada |
| S7 | E4 Recordatorios (US13-14) + E6 Encuesta (US19-20). Épicas con holgura | 18 | No | H5 Code freeze |
| S8 | E10 Analítica (US30-32) + inicio de Hardening (refactor). Holgura | 18 | Parcial | (sin hito) |
| S9 | Hardening y release: UAT productiva, carga de datos reales, documentación, reservas | n/a | Sí | H6 Go-live |

---

## 5. Gantt en texto (escala = sprints)

`#` = camino crítico, `.` = holgura, `R` = reserva (buffer)

```
Épica \ Sprint        S0  S1  S2  S3  S4  S5  S6  S7  S8  S9
Setup y diseño        #
E1 Auth + SIU             #
E8 Gestion activ.             #
E2 Descubrimiento                 #   #
E3 Inscripcion                        #
E9 Inscriptos (admin)                 .   .
E5 Asistencia                             #   #  R
E7 Progreso                                   #
E4 Recordatorios                                  .
E6 Encuesta                                       .
E10 Analitica                                         .
Hardening / Release                                   #   R
Hitos                 H0  H1  H2      H3      H4  H5      H6
```

---

## 6. Reservas (buffers)

Las reservas son tiempo adicional para subir la probabilidad de cumplir el plan. No son
relleno: se consumen solo ante un riesgo.

- **Contingencia sobre E5:** cubre el riesgo identificado del módulo crítico (integración
  con el SIU y persistencia transaccional bajo concurrencia en la carga de presencias).
- **Reserva de cronograma (S9):** colchón general para absorber atrasos acumulados del
  camino crítico antes del go-live, sin mover el hito H6.
- **Reserva de gestión (~10% global):** para imprevistos no contemplados (un recurso que
  baja, un bug mayor, un cambio de alcance del cliente). No está asignada a una tarea.

---

## 7. Resumen para la defensa

- El camino crítico es Setup, E1, E8, E2, E3, E5, E7, Hardening: la cadena de dependencias
  más larga, que define la duración mínima del proyecto.
- E5 ocupa dos sprints porque es la épica más grande (31 SP) y se parte en dos mitades
  secuenciales (parte 1 en S5, parte 2 en S6). No son dos alternativas.
- La holgura es el margen de las épicas que no están en el camino crítico (E9, E4, E6,
  E10): pueden correrse alrededor de un sprint sin mover el go-live.
- Las reservas (contingencia sobre E5, cronograma en S9, gestión 10%) absorben los riesgos
  sin tocar la fecha final.
