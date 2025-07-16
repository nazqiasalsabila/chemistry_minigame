import streamlit as st
from PIL import Image
import time
import random

# ---------- DATA UNSUR ----------
unsur_data = [
    {"simbol": "H", "nama": "Hidrogen"},
    {"simbol": "He", "nama": "Helium"},
    {"simbol": "Li", "nama": "Litium"},
    {"simbol": "Be", "nama": "Berilium"},
    {"simbol": "B", "nama": "Bor"},
    {"simbol": "C", "nama": "Karbon"},
    {"simbol": "N", "nama": "Nitrogen"},
    {"simbol": "O", "nama": "Oksigen"},
    {"simbol": "F", "nama": "Fluorin"},
    {"simbol": "Ne", "nama": "Neon"},
    {"simbol": "Na", "nama": "Natrium"},
    {"simbol": "Mg", "nama": "Magnesium"},
    {"simbol": "Al", "nama": "Aluminium"},
    {"simbol": "Si", "nama": "Silikon"},
    {"simbol": "P", "nama": "Fosfor"},
    {"simbol": "S", "nama": "Sulfur"},
    {"simbol": "Cl", "nama": "Klor"},
    {"simbol": "K", "nama": "Kalium"},
    {"simbol": "Ca", "nama": "Kalsium"},
    {"simbol": "Fe", "nama": "Besi"},
]

# ---------- INISIALISASI STATE ----------
if "halaman" not in st.session_state:
    st.session_state.halaman = "mulai"
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "hint_used" not in st.session_state:
    st.session_state.hint_used = False
if "soal_sekarang" not in st.session_state:
    st.session_state.soal_sekarang = None

# ---------- HALAMAN AWAL ----------
def halaman_mulai():
    banner = Image.open("assets/banner.png")
    st.image(banner, use_container_width=True)

    st.markdown("<h1 style='text-align:center;'>🎮 Periodic Table Quiz</h1>", unsafe_allow_
