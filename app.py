import streamlit as st
import random
import time

st.set_page_config(page_title="🚆 Juego de Trenes", layout="centered")

# =========================
# Estado del juego
# =========================
if "posicion" not in st.session_state:
    st.session_state.posicion = 0
    st.session_state.velocidad = 1
    st.session_state.estaciones = 10
    st.session_state.game_over = False

# =========================
# UI
# =========================
st.title("🚆 Juego de Trenes")
st.write("Lleva el tren hasta la última estación sin chocar.")

progress = st.progress(st.session_state.posicion / st.session_state.estaciones)

col1, col2, col3 = st.columns(3)

# =========================
# Controles
# =========================
with col1:
    if st.button("🚀 Acelerar") and not st.session_state.game_over:
        st.session_state.velocidad += 1

with col2:
    if st.button("🛑 Frenar") and not st.session_state.game_over:
        st.session_state.velocidad = max(1, st.session_state.velocidad - 1)

with col3:
    if st.button("▶ Avanzar") and not st.session_state.game_over:
        evento = random.random()

        # Evento aleatorio
        if evento < 0.2 and st.session_state.velocidad > 3:
            st.session_state.game_over = True
            st.error("💥 ¡Choque por exceso de velocidad!")
        else:
            st.session_state.posicion += st.session_state.velocidad

# =========================
# Estado del juego
# =========================
st.write(f"📍 Estación: {st.session_state.posicion}")
st.write(f"⚡ Velocidad: {st.session_state.velocidad}")

if st.session_state.posicion >= st.session_state.estaciones:
    st.success("🎉 ¡Llegaste al destino!")
    st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("🔄 Reiniciar juego"):
        st.session_state.posicion = 0
        st.session_state.velocidad = 1
        st.session_state.game_over = False
