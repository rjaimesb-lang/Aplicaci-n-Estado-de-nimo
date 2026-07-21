import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mood Music", page_icon="🎵", layout="centered")

# Título y descripción
st.title("🎵 Recomendador Musical")
st.write("Dime cómo te sientes hoy y te recomendaré la pista perfecta para este momento.")

st.divider()

# Selector de estado de ánimo
mood = st.selectbox(
    "¿Cuál es tu estado de ánimo actual?",
    ["Elige una opción...", "Feliz ☀️", "Relajado ☕", "Con Energía ⚡", "Melancólico 🌧️"]
)

# Lógica de recomendaciones
if mood == "Feliz ☀️":
    st.subheader("¡A disfrutar del día!")
    st.write("**Canción recomendada:** *Walking on Sunshine* - Katrina & The Waves")
    st.video("https://www.youtube.com/watch?v=iPUmE-tne5U")

elif mood == "Relajado ☕":
    st.subheader("Toma un respiro y relájate.")
    st.write("**Canción recomendada:** *Weightless* - Marconi Union")
    st.video("https://www.youtube.com/watch?v=UfcAVejslrU")

elif mood == "Con Energía ⚡":
    st.subheader("¡A comerse el mundo!")
    st.write("**Canción recomendada:** *Don't Stop Me Now* - Queen")
    st.video("https://www.youtube.com/watch?v=HgzGwKwLmgM")

elif mood == "Melancólico 🌧️":
    st.subheader("Un abrazo musical para ti.")
    st.write("**Canción recomendada:** *Someone Like You* - Adele")
    st.video("https://www.youtube.com/watch?v=hLQl3WQQoQ0")

else:
    st.info("👆 Selecciona un estado de ánimo en el menú desplegable para ver tu recomendación.")
