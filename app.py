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

# Data mode 2: Puzzle pilihan ganda
puzzle_data = [
    {"deskripsi": "Senyawa ini terdiri dari dua atom hidrogen dan satu oksigen", "jawaban": "H2O", "opsi": ["H2O", "O2", "NaCl", "CO2"]},
    {"deskripsi": "Gas rumah kaca utama yang dihasilkan dari pembakaran karbon", "jawaban": "CO2", "opsi": ["CO", "CH4", "CO2", "O2"]},
    {"deskripsi": "Senyawa dapur sehari-hari, terdiri dari Na dan Cl", "jawaban": "NaCl", "opsi": ["NaOH", "NaCl", "HCl", "KCl"]},
    {"deskripsi": "Asam kuat dalam lambung manusia", "jawaban": "HCl", "opsi": ["H2SO4", "CH3COOH", "HCl", "H2O"]},
    {"deskripsi": "Gas yang penting untuk respirasi manusia", "jawaban": "O2", "opsi": ["H2", "O3", "O2", "CO2"]},
    {"deskripsi": "Formula glukosa", "jawaban": "C6H12O6", "opsi": ["C6H12O6", "C2H5OH", "CH4", "CO"]},
    {"deskripsi": "Bahan bakar alkohol", "jawaban": "C2H5OH", "opsi": ["CH3COOH", "C2H5OH", "C6H6", "C2H6"]},
    {"deskripsi": "Senyawa amonia", "jawaban": "NH3", "opsi": ["NO2", "NH3", "N2O", "HNO3"]},
    {"deskripsi": "Asam asetat atau cuka", "jawaban": "CH3COOH", "opsi": ["CH3COOH", "H2CO3", "C2H5OH", "HCl"]},
    {"deskripsi": "Senyawa urea", "jawaban": "CH4N2O", "opsi": ["CH4N2O", "CH4", "NH3", "CO2"]},
]

# Data mode 3: Bingo istilah pilihan ganda
bingo_data = [
    {"istilah": "Mol", "deskripsi": "Satuan jumlah partikel zat", "opsi": ["Mol", "Ion", "Atom", "Proton"]},
    {"istilah": "Avogadro", "deskripsi": "Bilangan tetap 6.022e23", "opsi": ["Avogadro", "Dalton", "Massa", "Mol"]},
    {"istilah": "Larutan", "deskripsi": "Campuran homogen dua zat atau lebih", "opsi": ["Larutan", "Campuran", "Suspensi", "Koloid"]},
    {"istilah": "Ion", "deskripsi": "Atom yang bermuatan listrik", "opsi": ["Ion", "Atom", "Molekul", "Neutron"]},
    {"istilah": "Kovalent", "deskripsi": "Ikatan antar non-logam", "opsi": ["Ionik", "Kovalent", "Logam", "Polar"]},
    {"istilah": "Asam", "deskripsi": "Rasa masam, pH < 7", "opsi": ["Asam", "Basa", "Garam", "Netral"]},
    {"istilah": "Basa", "deskripsi": "Rasa pahit, pH > 7", "opsi": ["Asam", "Basa", "Netral", "Garam"]},
    {"istilah": "Reduksi", "deskripsi": "Reaksi pelepasan oksigen", "opsi": ["Oksidasi", "Reduksi", "Ionisasi", "Netralisasi"]},
    {"istilah": "Oksidasi", "deskripsi": "Reaksi penambahan oksigen", "opsi": ["Reduksi", "Oksidasi", "Ionisasi", "Degradasi"]},
    {"istilah": "Endoterm", "deskripsi": "Menyerap kalor", "opsi": ["Endoterm", "Eksoterm", "Isoterm", "Adiabatik"]},
]

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
    with col2:
        if st.button("Mulai Game 2"):
            st.session_state.mode = 2
            st.session_state.halaman = "main"
    with col3:
        if st.button("Mulai Game 3"):
            st.session_state.mode = 3
            st.session_state.halaman = "main"

# Halaman Main Game
if st.session_state.halaman == "main":
    st.markdown(f"### Babak {st.session_state.round} dari 10")
    bar = st.progress(0)
    for i in range(30):
        time.sleep(0.05)
        bar.progress((i + 1) / 30)

    if st.session_state.mode == 1:
        soal = random.choice(unsur_data)
        pilihan = random.sample([u["nama"] for u in unsur_data if u != soal], 3)
        pilihan.append(soal["nama"])
        random.shuffle(pilihan)
        st.subheader(f"Apa nama unsur dari simbol '{soal['simbol']}'?")
        jawaban = st.radio("", pilihan)

    elif st.session_state.mode == 2:
        soal = puzzle_data[st.session_state.round - 1]
        st.subheader(soal["deskripsi"])
        jawaban = st.radio("Pilih jawaban:", soal["opsi"])

    elif st.session_state.mode == 3:
        soal = bingo_data[st.session_state.round - 1]
        st.subheader(f"📘 {soal['deskripsi']}")
        jawaban = st.radio("Istilah Kimia:", soal["opsi"])

    if st.button("Kirim Jawaban"):
        benar = False
        if st.session_state.mode == 1:
            benar = (jawaban == soal["nama"])
        elif st.session_state.mode == 2:
            benar = (jawaban == soal["jawaban"])
        elif st.session_state.mode == 3:
            benar = (jawaban == soal["istilah"])

        if benar:
            st.success("Benar!")
            st.session_state.score += 10
            st.session_state.jawaban_benar += 1
        else:
            st.error("Salah!")
        st.session_state.round += 1

    if st.session_state.round > 10:
        st.session_state.halaman = "hasil"

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
