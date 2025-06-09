import streamlit as st


st.set_page_config(page_title="Quiz Interactivo", page_icon="🧠")

st.title("🧠 Quiz Interactivo Multitemático")
st.write("Responde las preguntas sobre programación, ciencia, historia y literatura.")


preguntas = [
    
    {"pregunta": "¿Qué lenguaje se ejecuta principalmente en navegadores web?", "opciones": ["Java", "Python", "JavaScript", "C++"], "respuesta_correcta": "JavaScript"},
    {"pregunta": "¿Qué significa 'IDE' en programación?", "opciones": ["Internet Development Environment", "Integrated Development Environment", "Internal Debugging Engine", "Intelligent Design Editor"], "respuesta_correcta": "Integrated Development Environment"},
    {"pregunta": "¿Cuál de estos es un lenguaje orientado a objetos?", "opciones": ["HTML", "Python", "SQL", "CSS"], "respuesta_correcta": "Python"},
    {"pregunta": "¿Qué estructura permite repetir instrucciones en programación?", "opciones": ["Condicional", "Bucle", "Variable", "Función"], "respuesta_correcta": "Bucle"},
    {"pregunta": "¿Qué símbolo se usa para comentar una línea en Python?", "opciones": ["//", "/*", "#", "--"], "respuesta_correcta": "#"},

    
    {"pregunta": "¿Cuál es la fórmula del agua?", "opciones": ["CO2", "H2O", "O2", "CH4"], "respuesta_correcta": "H2O"},
    {"pregunta": "¿Qué planeta es conocido como el planeta rojo?", "opciones": ["Marte", "Venus", "Júpiter", "Saturno"], "respuesta_correcta": "Marte"},
    {"pregunta": "¿Qué órgano humano bombea la sangre?", "opciones": ["Pulmón", "Riñón", "Corazón", "Hígado"], "respuesta_correcta": "Corazón"},
    {"pregunta": "¿Qué científico propuso la teoría de la relatividad?", "opciones": ["Newton", "Tesla", "Einstein", "Galileo"], "respuesta_correcta": "Einstein"},
    {"pregunta": "¿Cuál es la unidad básica de la vida?", "opciones": ["Átomo", "Célula", "Molécula", "Tejido"], "respuesta_correcta": "Célula"},

    
    {"pregunta": "¿En qué año llegó Cristóbal Colón a América?", "opciones": ["1492", "1500", "1512", "1485"], "respuesta_correcta": "1492"},
    {"pregunta": "¿Qué imperio construyó el Coliseo?", "opciones": ["Egipcio", "Romano", "Griego", "Inca"], "respuesta_correcta": "Romano"},
    {"pregunta": "¿Quién fue el primer presidente de los Estados Unidos?", "opciones": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"], "respuesta_correcta": "George Washington"},
    {"pregunta": "¿Dónde se firmó la Declaración de Independencia de EE. UU.?", "opciones": ["Boston", "Filadelfia", "Nueva York", "Washington D.C."], "respuesta_correcta": "Filadelfia"},
    {"pregunta": "¿En qué siglo fue la Revolución Francesa?", "opciones": ["XV", "XVI", "XVII", "XVIII"], "respuesta_correcta": "XVIII"},

    
    {"pregunta": "¿Quién escribió 'Cien años de soledad'?", "opciones": ["Mario Vargas Llosa", "Julio Cortázar", "Gabriel García Márquez", "Pablo Neruda"], "respuesta_correcta": "Gabriel García Márquez"},
    {"pregunta": "¿Cuál es la obra más famosa de Miguel de Cervantes?", "opciones": ["La Odisea", "El Quijote", "Fausto", "La Ilíada"], "respuesta_correcta": "El Quijote"},
    {"pregunta": "¿Qué poeta escribió '20 poemas de amor y una canción desesperada'?", "opciones": ["Neruda", "Borges", "Benedetti", "Machado"], "respuesta_correcta": "Neruda"},
    {"pregunta": "¿Qué género literario es una narración breve con moraleja?", "opciones": ["Fábula", "Poema", "Ensayo", "Novela"], "respuesta_correcta": "Fábula"},
    {"pregunta": "¿Cuál de estos escritores fue peruano?", "opciones": ["Julio Cortázar", "Gabriel García Márquez", "Mario Vargas Llosa", "Pablo Neruda"], "respuesta_correcta": "Mario Vargas Llosa"},
]


if "puntuacion" not in st.session_state:
    st.session_state.puntuacion = 0
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0


def siguiente_pregunta(seleccion):
    correcta = preguntas[st.session_state.pregunta_actual]["respuesta_correcta"]
    if seleccion == correcta:
        st.session_state.puntuacion += 1
    st.session_state.pregunta_actual += 1


if st.session_state.pregunta_actual < len(preguntas):
    actual = preguntas[st.session_state.pregunta_actual]
    st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1} de {len(preguntas)}")
    st.write(actual["pregunta"])
    seleccion = st.radio("Selecciona una opción:", actual["opciones"], key=f"pregunta{st.session_state.pregunta_actual}")
    if st.button("Responder"):
        siguiente_pregunta(seleccion)
        st.rerun()
else:
    st.success(f"🎉 ¡Has completado el quiz! Tu puntaje fue: {st.session_state.puntuacion} / {len(preguntas)}")
    if st.button("Reiniciar Quiz"):
        st.session_state.pregunta_actual = 0
        st.session_state.puntuacion = 0
        st.rerun()
