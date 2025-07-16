import streamlit as st
import random
import time

# Inisialisasi session state
if "halaman" not in st.session_state:
    st.session_state.halaman = "menu"
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "mode" not in st.session_state:
    st.session_state.mode = None
if "hint_used" not in st.session_state:
    st.session_state.hint_used = False
if "jawaban_benar" not in st.session_state:
    st.session_state.jawaban_benar = 0
if "soal_sudah_dijawab" not in st.session_state:
    st.session_state.soal_sudah_dijawab = False

# Data mode 1: Tebak nama unsur
unsur_data = [
    {"simbol": "H", "nama": "Hidrogen"},
    {"simbol": "O", "nama": "Oksigen"},
    {"simbol": "Na", "nama": "Natrium"},
    {"simbol": "Cl", "nama": "Klor"},
    {"simbol": "C", "nama": "Karbon"},
    {"simbol": "Fe", "nama": "Besi"},
    {"simbol": "Au", "nama": "Emas"},
    {"simbol": "Ag", "nama": "Perak"},
    {"simbol": "Mg", "nama": "Magnesium"},
    {"simbol": "Ca", "nama": "Kalsium"},
]

# Placeholder data mode 2 dan 3 (isi sesuai data sebelumnya jika ada)
puzzle_data = []
bingo_data = []

# Halaman Menu
if st.session_state.halaman == "menu":
    st.markdown("""
        <h1 style='text-align:center;'>🎮 Chemistry Quiz</h1>
        <p style='text-align:center;'>Tebak nama unsur, struktur senyawa, dan istilah kimia!</p>
        <p style='text-align:center;'>🔹 10 babak | ⏱️ 30 detik per babak | 💯 Total skor: 100</p>
        <p style='text-align:center;'>💡 Hint tersedia 1x per game</p>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Mulai Game 1"):
            st.session_state.mode = 1
            st.session_state.halaman = "main"
            st.session_state.soal_sudah_dijawab = False
    with col2:
        if st.button("Mulai Game 2"):
            st.session_state.mode = 2
            st.session_state.halaman = "main"
            st.session_state.soal_sudah_dijawab = False
    with col3:
        if st.button("Mulai Game 3"):
            st.session_state.mode = 3
            st.session_state.halaman = "main"
            st.session_state.soal_sudah_dijawab = False

# Halaman Main Game
if st.session_state.halaman == "main":
    st.markdown(f"### Babak {st.session_state.round} dari 10")
    bar = st.progress(0)
    for i in range(30):
        time.sleep(0.05)
        bar.progress((i + 1) / 30)

    if st.session_state.soal_sudah_dijawab:
        st.info("Jawaban sudah dikirim. Tunggu babak berikutnya...")
        st.stop()

    soal = None
    pilihan = []

    if st.session_state.mode == 1:
        soal = random.choice(unsur_data)
        pilihan = random.sample([u["nama"] for u in unsur_data if u != soal], 3)
        pilihan.append(soal["nama"])
        random.shuffle(pilihan)
        st.subheader(f"Apa nama unsur dari simbol '{soal['simbol']}'?")

    elif st.session_state.mode == 2:
        soal = puzzle_data[st.session_state.round - 1]
        pilihan = soal["opsi"][:]
        random.shuffle(pilihan)
        st.subheader(soal["deskripsi"])

    elif st.session_state.mode == 3:
        soal = bingo_data[st.session_state.round - 1]
        pilihan = soal["opsi"][:]
        random.shuffle(pilihan)
        st.subheader(f"📘 {soal['deskripsi']}")

    selected = st.radio("Pilih jawaban:", pilihan, key=f"jawaban_{st.session_state.round}")

    if st.button("Kirim Jawaban") and not st.session_state.soal_sudah_dijawab:
        benar = False
        if st.session_state.mode == 1:
            benar = (selected == soal["nama"])
        elif st.session_state.mode == 2:
            benar = (selected == soal["jawaban"])
        elif st.session_state.mode == 3:
            benar = (selected == soal["istilah"])

        if benar:
            st.session_state.score += 10
            st.session_state.jawaban_benar += 1

        st.session_state.soal_sudah_dijawab = True

        if st.session_state.round == 10:
            st.session_state.halaman = "hasil"
        else:
            st.session_state.round += 1
            st.session_state.soal_sudah_dijawab = False
            st.experimental_rerun()

# Halaman Hasil
if st.session_state.halaman == "hasil":
    st.balloons()
    st.markdown(f"## 🎉 Skor Akhir: {st.session_state.score} / 100")
    st.markdown(f"Jawaban Benar: {st.session_state.jawaban_benar} dari 10")
    if st.button("Main Lagi 🔁"):
        st.session_state.halaman = "menu"
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.jawaban_benar = 0
        st.session_state.hint_used = False
        st.session_state.soal_sudah_dijawab = False
