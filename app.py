import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mood Music", page_icon="🎵", layout="centered")

# Inyección de CSS para el fondo rosado y textura
estilo_fondo = """
<style>
.stApp {
    background-color: #ffe6eb; /* Color de fondo rosado pastel */
    background-image: radial-gradient(#ffb3c6 1.5px, transparent 1.5px); /* Textura de puntitos */
    background-size: 25px 25px; /* Tamaño de la textura */
}
</style>
"""
st.markdown(estilo_fondo, unsafe_allow_html=True)

# Título y descripción
st.title("🎵 Recomendador Musical Múltiple")
st.write("Dime cómo te sientes hoy y te daré varias opciones perfectas para este momento.")

st.divider()

# Selector de estado de ánimo
mood = st.selectbox(
    "¿Cuál es tu estado de ánimo actual?",
    [
        "Elige una opción...", 
        "Feliz ☀️", 
        "Relajado ☕", 
        "Con Energía ⚡", 
        "Melancólico 🌧️",
        "Enojado 😡",
        "Enamorado 🥰",
        "Concentrado 🧠"
    ]
)

# Lógica de recomendaciones con múltiples opciones
if mood == "Feliz ☀️":
    st.subheader("¡A disfrutar del día! Aquí tienes tus opciones:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Walking on Sunshine* - Katrina & The Waves")
        st.video("https://www.youtube.com/watch?v=iPUmE-tne5U")
    with tab2:
        st.write("**Canción:** *Happy* - Pharrell Williams")
        st.video("https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    with tab3:
        st.write("**Canción:** *Don't Worry Be Happy* - Bobby McFerrin")
        st.video("https://www.youtube.com/watch?v=d-diB65scQU")

elif mood == "Relajado ☕":
    st.subheader("Toma un respiro y relájate con estas pistas:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Weightless* - Marconi Union")
        st.video("https://www.youtube.com/watch?v=UfcAVejslrU")
    with tab2:
        st.write("**Canción:** *Sunrise* - Norah Jones")
        st.video("https://www.youtube.com/watch?v=fd02pGJx0s0")
    with tab3:
        st.write("**Canción:** *Banana Pancakes* - Jack Johnson")
        st.video("https://www.youtube.com/watch?v=OkyrIRyrRdY")

elif mood == "Con Energía ⚡":
    st.subheader("¡A comerse el mundo! Sube el volumen:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Don't Stop Me Now* - Queen")
        st.video("https://www.youtube.com/watch?v=HgzGwKwLmgM")
    with tab2:
        st.write("**Canción:** *Eye of the Tiger* - Survivor")
        st.video("https://www.youtube.com/watch?v=btPJPFnesV4")
    with tab3:
        st.write("**Canción:** *Can't Stop* - Red Hot Chili Peppers")
        st.video("https://www.youtube.com/watch?v=8DyziWtkfBw")

elif mood == "Melancólico 🌧️":
    st.subheader("Un abrazo musical para ti. Escucha esto:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Someone Like You* - Adele")
        st.video("https://www.youtube.com/watch?v=hLQl3WQQoQ0")
    with tab2:
        st.write("**Canción:** *Fix You* - Coldplay")
        st.video("https://www.youtube.com/watch?v=k4V3Mo61fJM")
    with tab3:
        st.write("**Canción:** *Let It Be* - The Beatles")
        st.video("https://www.youtube.com/watch?v=QDYfEBY9NM4")

elif mood == "Enojado 😡":
    st.subheader("¡Saca toda esa frustración! Un poco de rock ayuda:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Smells Like Teen Spirit* - Nirvana")
        st.video("https://www.youtube.com/watch?v=hTWKbfoikeg")
    with tab2:
        st.write("**Canción:** *Killing In The Name* - Rage Against The Machine")
        st.video("https://www.youtube.com/watch?v=bWXazVhlyxQ")
    with tab3:
        st.write("**Canción:** *Break Stuff* - Limp Bizkit")
        st.video("https://www.youtube.com/watch?v=ZpUYjpKg9KY")

elif mood == "Enamorado 🥰":
    st.subheader("El amor está en el aire. Disfruta estas melodías románticas:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Perfect* - Ed Sheeran")
        st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
    with tab2:
        st.write("**Canción:** *All of Me* - John Legend")
        st.video("https://www.youtube.com/watch?v=450p7goxZqg")
    with tab3:
        st.write("**Canción:** *Just The Way You Are* - Bruno Mars")
        st.video("https://www.youtube.com/watch?v=LjhCEhWiKXk")

elif mood == "Concentrado 🧠":
    st.subheader("Modo enfoque activado. Ideal para estudiar o trabajar:")
    tab1, tab2, tab3 = st.tabs(["Opción 1", "Opción 2", "Opción 3"])
    
    with tab1:
        st.write("**Canción:** *Lofi Hip Hop Radio* - Lofi Girl")
        st.video("https://www.youtube.com/watch?v=jfKfPfyJRdk")
    with tab2:
        st.write("**Canción:** *Experience* - Ludovico Einaudi")
        st.video("https://www.youtube.com/watch?v=hN_q-_nGv4U")
    with tab3:
        st.write("**Canción:** *Clair de Lune* - Claude Debussy")
        st.video("https://www.youtube.com/watch?v=WNcsUNKlAKw")

else:
    st.info("👆 Selecciona un estado de ánimo en el menú desplegable para ver tus recomendaciones.")
