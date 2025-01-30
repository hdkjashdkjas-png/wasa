import streamlit as st
import random
import time

# Base de datos de preguntas (personalizable)
preguntas_por_tema = {
    "Razonamiento verbal": [
        {
            "pregunta": "¿Qué palabra es sinónimo de 'efímero'?",
            "opciones": ["A) Perdurable", "B) Transitorio", "C) Eterno", "D) Persistente"],
            "respuesta": "B"
        },
        {
            "pregunta": "Elija el antónimo de 'prudente':",
            "opciones": ["A) Cauto", "B) Sensato", "C) Imprudente", "D) Juicioso"],
            "respuesta": "C"
        },
        {
            "pregunta": "Complete la analogía: LIBRO es a LEER como PELÍCULA es a...",
            "opciones": ["A) Director", "B) Actor", "C) Ver", "D) Guión"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué palabra completa mejor la oración? 'A pesar de su ____, logró terminar el proyecto a tiempo.'",
            "opciones": ["A) experiencia", "B) ineptitud", "C) juventud", "D) inexperiencia"],
            "respuesta": "D"
        },
        {
            "pregunta": "Identifique el error en la frase: 'El principio de la escuela fue muy estricto con la disciplina.'",
            "opciones": ["A) principio", "B) escuela", "C) estricto", "D) disciplina"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué palabra no pertenece al grupo?",
            "opciones": ["A) Silla", "B) Mesa", "C) Sofá", "D) Martillo"],
            "respuesta": "D"
        },
        {
            "pregunta": "Sinónimo de 'lúgubre':",
            "opciones": ["A) Brillante", "B) Alegre", "C) Sombrío", "D) Colorido"],
            "respuesta": "C"
        },
        {
            "pregunta": "Antónimo de 'amplio':",
            "opciones": ["A) Espacioso", "B) Estrecho", "C) Ancho", "D) Generoso"],
            "respuesta": "B"
        },
        {
            "pregunta": "Analogía: MÉDICO es a HOSPITAL como JUEZ es a...",
            "opciones": ["A) Corte", "B) Abogado", "C) Tribunal", "D) Ley"],
            "respuesta": "C"
        },
        {
            "pregunta": "Complete la oración: 'El científico presentó una teoría ____ que revolucionó su campo de estudio.'",
            "opciones": ["A) obsoleta", "B) innovadora", "C) copiada", "D) trivial"],
            "respuesta": "B"
        },
        {
            "pregunta": "Identifique el error: 'Los datos había sido alterados antes de la auditoría.'",
            "opciones": ["A) datos", "B) había", "C) alterados", "D) auditoría"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué palabra es sinónimo de 'sagaz'?",
            "opciones": ["A) Tonto", "B) Astuto", "C) Lento", "D) Grosero"],
            "respuesta": "B"
        },
        {
            "pregunta": "Antónimo de 'altruista':",
            "opciones": ["A) Generoso", "B) Egoísta", "C) Solidario", "D) Compasivo"],
            "respuesta": "B"
        },
        {
            "pregunta": "Relacione: PINTOR es a CUADRO como ESCRITOR es a...",
            "opciones": ["A) Libro", "B) Novela", "C) Poema", "D) Pluma"],
            "respuesta": "B"
        },
        {
            "pregunta": "Complete: 'Si no ____ más atención, reprobarás el examen.'",
            "opciones": ["A) prestas", "B) presta", "C) prestan", "D) presten"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué expresión está mal escrita?",
            "opciones": ["A) Concienciar", "B) Vinistes", "C) Hubieron", "D) Haiga"],
            "respuesta": "B"
        },
        {
            "pregunta": "Sinónimo de 'cándido':",
            "opciones": ["A) Malicioso", "B) Inocente", "C) Experto", "D) Cínico"],
            "respuesta": "B"
        },
        {
            "pregunta": "Antónimo de 'ferviente':",
            "opciones": ["A) Apasionado", "B) Indiferente", "C) Ardiente", "D) Entusiasta"],
            "respuesta": "B"
        },
        {
            "pregunta": "Analogía: AGUA es a SACIAR como COMIDA es a...",
            "opciones": ["A) Masticar", "B) Beber", "C) Alimentar", "D) Cocinar"],
            "respuesta": "C"
        },
        {
            "pregunta": "Complete: 'La conferencia fue tan ____ que varios asistentes se durmieron.'",
            "opciones": ["A) emocionante", "B) dinámica", "C) monótona", "D) interesante"],
            "respuesta": "C"
        },
        {
            "pregunta": "Identifique el error: 'Hubieron muchos problemas técnicos durante la presentación.'",
            "opciones": ["A) Hubieron", "B) problemas", "C) técnicos", "D) presentación"],
            "respuesta": "A"
        },
        {
            "pregunta": "Sinónimo de 'ínfimo':",
            "opciones": ["A) Enorme", "B) Minúsculo", "C) Superior", "D) Promedio"],
            "respuesta": "B"
        },
        {
            "pregunta": "Antónimo de 'preciso':",
            "opciones": ["A) Exacto", "B) Impreciso", "C) Correcto", "D) Certero"],
            "respuesta": "B"
        },
        {
            "pregunta": "Relacione: ÁRBOL es a BOSQUE como ESTRELLA es a...",
            "opciones": ["A) Cielo", "B) Universo", "C) Galaxia", "D) Noche"],
            "respuesta": "C"
        },
        {
            "pregunta": "Complete: 'El joven, ____ a las críticas, siguió adelante con su proyecto.'",
            "opciones": ["A) atento", "B) sensible", "C) ajeno", "D) receptivo"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué palabra es incorrecta?",
            "opciones": ["A) Travieso", "B) Anduve", "C) Vinistes", "D) Dijeron"],
            "respuesta": "C"
        },
        {
            "pregunta": "Sinónimo de 'prolijidad':",
            "opciones": ["A) Descuidado", "B) Meticulosidad", "C) Desorden", "D) Negligencia"],
            "respuesta": "B"
        },
        {
            "pregunta": "Antónimo de 'opaco':",
            "opciones": ["A) Brillante", "B) Transparente", "C) Turbio", "D) Mate"],
            "respuesta": "B"
        },
        {
            "pregunta": "Analogía: CALOR es a TERMÓMETRO como VIENTO es a...",
            "opciones": ["A) Barómetro", "B) Anemómetro", "C) Higrómetro", "D) Pluviómetro"],
            "respuesta": "B"
        },
        {
            "pregunta": "Complete: 'Aunque el equipo ____ trabajado mucho, no ganó el campeonato.'",
            "opciones": ["A) había", "B) habían", "C) hayan", "D) hubieron"],
            "respuesta": "A"
        },
        {
            "pregunta": "Identifique el error: 'Debes de llegar temprano para conseguir buenos asientos.'",
            "opciones": ["A) Debes", "B) de", "C) llegar", "D) asientos"],
            "respuesta": "B"
        }
    ],

    "Razonamiento lógico": [
        {
            "pregunta": "¿Qué número sigue en la secuencia: 2, 4, 6, 8, ___?",
            "opciones": ["A) 9", "B) 10", "C) 12", "D) 14"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si todos los gatos son animales y algunos animales son domésticos, entonces:",
            "opciones": ["A) Todos los gatos son domésticos", "B) Algunos gatos son domésticos", "C) Ningún gato es doméstico", "D) Todos los domésticos son gatos"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué figura completa la serie? (Imagina un cuadrado, luego un círculo, luego un triángulo, luego...)",
            "opciones": ["A) Cuadrado", "B) Círculo", "C) Triángulo", "D) Rectángulo"],
            "respuesta": "A"
        },
        {
            "pregunta": "Si 3 manzanas cuestan $6, ¿cuánto cuestan 5 manzanas?",
            "opciones": ["A) $8", "B) $10", "C) $12", "D) $15"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número falta en la secuencia: 5, 10, 15, ___, 25?",
            "opciones": ["A) 18", "B) 20", "C) 22", "D) 24"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si A = 1, B = 2, C = 3, ¿cuál es el valor de A + B + C?",
            "opciones": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué palabra no pertenece al grupo?",
            "opciones": ["A) Perro", "B) Gato", "C) Pájaro", "D) Mesa"],
            "respuesta": "D"
        },
        {
            "pregunta": "Si hoy es lunes, ¿qué día será dentro de 5 días?",
            "opciones": ["A) Viernes", "B) Sábado", "C) Domingo", "D) Lunes"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número sigue en la secuencia: 1, 3, 5, 7, ___?",
            "opciones": ["A) 8", "B) 9", "C) 10", "D) 11"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si 2 + 2 = 4 y 3 + 3 = 6, ¿cuánto es 4 + 4?",
            "opciones": ["A) 6", "B) 8", "C) 10", "D) 12"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué figura completa la analogía? (Círculo es a redondo como cuadrado es a...)",
            "opciones": ["A) Triangular", "B) Cuadrangular", "C) Rectangular", "D) Circular"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si un reloj marca las 3:15, ¿qué ángulo forman las manecillas?",
            "opciones": ["A) 0°", "B) 7.5°", "C) 15°", "D) 30°"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número falta en la secuencia: 10, 20, 30, ___, 50?",
            "opciones": ["A) 35", "B) 40", "C) 45", "D) 55"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si 5 personas pueden pintar una casa en 3 días, ¿cuántos días tardarán 10 personas?",
            "opciones": ["A) 1.5", "B) 3", "C) 6", "D) 12"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué palabra completa la analogía? (Libro es a leer como película es a...)",
            "opciones": ["A) Ver", "B) Escuchar", "C) Tocar", "D) Oler"],
            "respuesta": "A"
        },
        {
            "pregunta": "Si 4 + 4 = 8 y 5 + 5 = 10, ¿cuánto es 6 + 6?",
            "opciones": ["A) 10", "B) 12", "C) 14", "D) 16"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número sigue en la secuencia: 12, 24, 36, ___?",
            "opciones": ["A) 42", "B) 48", "C) 54", "D) 60"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si un tren viaja a 60 km/h, ¿cuánto tiempo tardará en recorrer 120 km?",
            "opciones": ["A) 1 hora", "B) 1.5 horas", "C) 2 horas", "D) 2.5 horas"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué palabra no pertenece al grupo?",
            "opciones": ["A) Rojo", "B) Verde", "C) Azul", "D) Manzana"],
            "respuesta": "D"
        },
        {
            "pregunta": "Si 3 + 3 = 6 y 4 + 4 = 8, ¿cuánto es 5 + 5?",
            "opciones": ["A) 8", "B) 10", "C) 12", "D) 14"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número falta en la secuencia: 7, 14, 21, ___, 35?",
            "opciones": ["A) 24", "B) 28", "C) 30", "D) 32"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si un cuadrado tiene un lado de 4 cm, ¿cuál es su perímetro?",
            "opciones": ["A) 8 cm", "B) 12 cm", "C) 16 cm", "D) 20 cm"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué palabra completa la analogía? (Cielo es a azul como hierba es a...)",
            "opciones": ["A) Rojo", "B) Verde", "C) Amarillo", "D) Azul"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si 6 + 6 = 12 y 7 + 7 = 14, ¿cuánto es 8 + 8?",
            "opciones": ["A) 14", "B) 16", "C) 18", "D) 20"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número sigue en la secuencia: 9, 18, 27, ___?",
            "opciones": ["A) 32", "B) 36", "C) 40", "D) 45"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si un auto recorre 100 km en 2 horas, ¿cuál es su velocidad promedio?",
            "opciones": ["A) 40 km/h", "B) 50 km/h", "C) 60 km/h", "D) 70 km/h"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué palabra no pertenece al grupo?",
            "opciones": ["A) Piano", "B) Guitarra", "C) Violín", "D) Libro"],
            "respuesta": "D"
        },
        {
            "pregunta": "Si 8 + 8 = 16 y 9 + 9 = 18, ¿cuánto es 10 + 10?",
            "opciones": ["A) 18", "B) 20", "C) 22", "D) 24"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué número falta en la secuencia: 11, 22, 33, ___, 55?",
            "opciones": ["A) 40", "B) 44", "C) 48", "D) 50"],
            "respuesta": "B"
        },
        {
            "pregunta": "Si un triángulo tiene tres lados, ¿cuántos lados tiene un cuadrado?",
            "opciones": ["A) 2", "B) 3", "C) 4", "D) 5"],
            "respuesta": "C"
        }
    ]
}

# Configurar la página
st.set_page_config(page_title="Simulador de Examen psicométrico (verbal)", layout="centered")
st.title("📚 Simulador de Exámen")

# Inicializar el estado de la sesión
if "preguntas" not in st.session_state:
    st.session_state.preguntas = []
if "indice_pregunta" not in st.session_state:
    st.session_state.indice_pregunta = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "mostrar_feedback" not in st.session_state:
    st.session_state.mostrar_feedback = False
if "answered" not in st.session_state:
    st.session_state.answered = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "end_time" not in st.session_state:
    st.session_state.end_time = None
if "examen_iniciado" not in st.session_state:
    st.session_state.examen_iniciado = False
if "preguntas_incorrectas" not in st.session_state:
    st.session_state.preguntas_incorrectas = []

# Función para mostrar el temporizador
def mostrar_temporizador():
    if st.session_state.start_time is not None:
        elapsed_time = time.time() - st.session_state.start_time
        minutos = int(elapsed_time // 60)
        segundos = int(elapsed_time % 60)
        return f"Tiempo transcurrido: {minutos}:{segundos:02d}"
    return "Tiempo transcurrido: 0:00"

# Función para calcular la duración del examen
def calcular_duracion_examen():
    if st.session_state.start_time is not None and st.session_state.end_time is not None:
        duracion = st.session_state.end_time - st.session_state.start_time
        minutos = int(duracion // 60)
        segundos = int(duracion % 60)
        return f"{minutos}:{segundos:02d}"
    return "0:00"

# Selección de tema y botón para iniciar el examen
if not st.session_state.examen_iniciado:
    tema_seleccionado = st.selectbox("Elige un tema:", list(preguntas_por_tema.keys()))
    if st.button("Comenzar Examen"):
        st.session_state.preguntas = random.sample(preguntas_por_tema[tema_seleccionado], k=len(preguntas_por_tema[tema_seleccionado]))
        st.session_state.indice_pregunta = 0
        st.session_state.puntaje = 0
        st.session_state.mostrar_feedback = False
        st.session_state.answered = False
        st.session_state.start_time = time.time()
        st.session_state.end_time = None
        st.session_state.examen_iniciado = True
        st.session_state.preguntas_incorrectas = []
        st.rerun()

# Contenedor principal para preguntas
main_container = st.container()

# Mostrar preguntas si hay en progreso
if st.session_state.preguntas and st.session_state.examen_iniciado:
    pregunta_actual = st.session_state.preguntas[st.session_state.indice_pregunta]
    
    with main_container:
        st.subheader(f"Pregunta {st.session_state.indice_pregunta + 1}:")
        st.markdown(f"**{pregunta_actual['pregunta']}**")
        
        # Mostrar opciones en columnas (solo interactivas si no se ha respondido)
        cols = st.columns(4)
        for i, opcion in enumerate(pregunta_actual["opciones"]):
            with cols[i % 4]:
                if st.button(opcion, key=f"opcion_{i}", disabled=st.session_state.answered):
                    if not st.session_state.answered:  # Solo procesar si no se ha respondido
                        if opcion[0] == pregunta_actual["respuesta"]:
                            st.session_state.puntaje += 1
                            st.session_state.mostrar_feedback = "correcto"
                        else:
                            st.session_state.mostrar_feedback = "incorrecto"
                            # Guardar la pregunta incorrecta con el texto completo de la respuesta
                            st.session_state.preguntas_incorrectas.append({
                                "pregunta": pregunta_actual["pregunta"],
                                "respuesta_correcta": next(opc for opc in pregunta_actual["opciones"] if opc[0] == pregunta_actual["respuesta"]),
                                "respuesta_usuario": opcion
                            })
                        
                        st.session_state.answered = True
                        st.rerun()

    # Contenedor para feedback y navegación
    feedback_container = st.empty()
    
    if st.session_state.mostrar_feedback and st.session_state.answered:
        with feedback_container:
            # Mostrar feedback
            if st.session_state.mostrar_feedback == "correcto":
                st.success("✅ Correcto!")
            elif st.session_state.mostrar_feedback == "incorrecto":
                st.error(f"❌ Incorrecto. La respuesta correcta es {next(opc for opc in pregunta_actual['opciones'] if opc[0] == pregunta_actual['respuesta'])}.")
            
            # Botón para siguiente pregunta
            if st.session_state.indice_pregunta < len(st.session_state.preguntas) - 1:
                if st.button("Siguiente pregunta →"):
                    st.session_state.indice_pregunta += 1
                    st.session_state.answered = False
                    st.session_state.mostrar_feedback = False
                    st.rerun()
            else:
                if st.button("Finalizar Examen"):
                    st.session_state.end_time = time.time()  # Registrar el tiempo de finalización
                    st.session_state.mostrar_feedback = "finalizado"
                    st.rerun()

    # Mostrar resultados finales
    if st.session_state.mostrar_feedback == "finalizado":
        st.balloons()
        with st.expander("🏆 **Resultado Final**", expanded=True):
            st.markdown(f"""
            <div style='background-color:#353535; padding:20px; border-radius:10px;'>
                <h3 style='color:#1f6feb;'>Examen Terminado!</h3>
                <p>Puntaje final: <strong>{st.session_state.puntaje}/{len(st.session_state.preguntas)}</strong></p>
                <p>Tiempo total: <strong>{calcular_duracion_examen()}</strong></p>
            </div>
            """, unsafe_allow_html=True)

            # Mostrar preguntas incorrectas con el texto completo de las respuestas
            if st.session_state.preguntas_incorrectas:
                st.markdown("### 📝 Preguntas incorrectas:")
                for idx, pregunta_incorrecta in enumerate(st.session_state.preguntas_incorrectas, start=1):
                    st.markdown(f"""
                    <div style='background-color:#2a2a2a; padding:10px; border-radius:5px; margin-bottom:10px;'>
                        <p><strong>Pregunta {idx}:</strong> {pregunta_incorrecta["pregunta"]}</p>
                        <p><strong>Tu respuesta:</strong> {pregunta_incorrecta["respuesta_usuario"]}</p>
                        <p><strong>Respuesta correcta:</strong> {pregunta_incorrecta["respuesta_correcta"]}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.success("¡Felicidades! No tuviste ninguna pregunta incorrecta. 🎉")

        st.session_state.preguntas = []
        st.session_state.examen_iniciado = False

    # Barra de progreso
    if st.session_state.preguntas:
        progreso = st.session_state.indice_pregunta / len(st.session_state.preguntas)
        st.progress(progreso)

    # Mostrar temporizador en tiempo real
    temporizador_placeholder = st.empty()
    while st.session_state.examen_iniciado and not st.session_state.mostrar_feedback == "finalizado":
        temporizador_placeholder.markdown(f"**{mostrar_temporizador()}**")
        time.sleep(1)  # Actualizar cada segundo

else:
    st.warning("Elige un tema y haz clic en **Comenzar Examen**.")