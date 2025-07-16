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

# Data mode 2: Puzzle struktur (tanpa gambar, sebagai deskripsi teks)
puzzle_data = [
    {"deskripsi": "Senyawa ini terdiri dari dua atom hidrogen dan satu oksigen", "jawaban": "H2O"},
    {"deskripsi": "Gas rumah kaca utama yang dihasilkan dari pembakaran karbon", "jawaban": "CO2"},
    {"deskripsi": "Senyawa dapur sehari-hari, terdiri dari Na dan Cl", "jawaban": "NaCl"},
    {"deskripsi": "Asam kuat dalam lambung manusia", "jawaban": "HCl"},
    {"deskripsi": "Gas yang penting untuk respirasi manusia", "jawaban": "O2"},
    {"deskripsi": "Senyawa yang terdiri dari karbon, hidrogen dan oksigen, formula glukosa", "jawaban": "C6H12O6"},
    {"deskripsi": "Bahan bakar alkohol", "jawaban": "C2H5OH"},
    {"deskripsi": "Senyawa amonia", "jawaban": "NH3"},
    {"deskripsi": "Asam asetat atau cuka", "jawaban": "CH3COOH"},
    {"deskripsi": "Senyawa urea", "jawaban": "CH4N2O"},
]

# Data mode 3: Bingo istilah
bingo_data = [
    {"istilah": "Mol", "deskripsi": "Satuan jumlah partikel zat"},
    {"istilah": "Avogadro", "deskripsi": "Bilangan tetap 6.022e23"},
    {"istilah": "Larutan", "deskripsi": "Campuran homogen dua zat atau lebih"},
    {"istilah": "Ion", "deskripsi": "Atom yang bermuatan listrik"},
    {"istilah": "Kovalent", "deskripsi": "Ikatan antar non-logam"},
    {"istilah": "Asam", "deskripsi": "Rasa masam, pH < 7"},
    {"istilah": "Basa", "deskripsi": "Rasa pahit, pH > 7"},
    {"istilah": "Reduksi", "deskripsi": "Reaksi pelepasan oksigen"},
    {"istilah": "Oksidasi", "deskripsi": "Reaksi penambahan oksigen"},
    {"istilah": "Endoterm", "deskripsi": "Menyerap kalor"},
]

# Halaman Menu
if st.session_state.halaman == "menu":
    st.markdown("""
        <h1 style='text-align:center;'>🎮 Periodic Table Quiz</h1>
        <p style='text-align:center;'>Tebak nama unsur, struktur senyawa, dan istilah kimia!</p>
        <p style='text-align:center;'>🔹 10 babak | ⏱️ 30 detik per babak | 💯 Total skor: 100</p>
        <p style='text-align:center;'>💡 Hint tersedia 1x per game</p>
    """, unsafe_allow_html=True)
    st.write("\n")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Mulai Game 1 🧪"):
            st.session_state.mode = 1
            st.session_state.halaman = "main"
    with col2:
        if st.button("Mulai Game 2 🧩"):
            st.session_state.mode = 2
            st.session_state.halaman = "main"
    with col3:
        if st.button("Mulai Game 3 🧠"):
            st.session_state.mode = 3
            st.session_state.halaman = "main"

# Halaman Main Game
if st.session_state.halaman == "main":
    st.markdown(f"### Babak {st.session_state.round} dari 10")

    # Timer (hanya visual)
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

        if st.button("Kirim Jawaban"):
            if jawaban == soal["nama"]:
                st.success("Benar!")
                st.session_state.score += 10
                st.session_state.jawaban_benar += 1
            else:
                st.error(f"Salah! Jawaban yang benar: {soal['nama']}")
            st.session_state.round += 1

    elif st.session_state.mode == 2:
        soal = puzzle_data[st.session_state.round - 1]
        st.write(soal["deskripsi"])
        jawaban = st.text_input("Jawabanmu (contoh: H2O)")

        if st.button("Kirim Jawaban"):
            if jawaban.strip().upper() == soal["jawaban"].upper():
                st.success("Benar!")
                st.session_state.score += 10
                st.session_state.jawaban_benar += 1
            else:
                st.error(f"Salah! Jawaban benar: {soal['jawaban']}")
            st.session_state.round += 1

    elif st.session_state.mode == 3:
        soal = bingo_data[st.session_state.round - 1]
        st.write(f"📘 {soal['deskripsi']}")
        jawaban = st.text_input("Istilah Kimia")

        if st.button("Kirim Jawaban"):
            if jawaban.strip().lower() == soal["istilah"].lower():
                st.success("Benar!")
                st.session_state.score += 10
                st.session_state.jawaban_benar += 1
            else:
                st.error(f"Salah! Jawaban benar: {soal['istilah']}")
            st.session_state.round += 1

    if st.session_state.round > 10:
        st.session_state.halaman = "hasil"

# Halaman Akhir
if st.session_state.halaman == "hasil":
    st.balloons()
    st.markdown(f"""
    ## 🎉 Skor Akhir: {st.session_state.score} / 100
    Jumlah Jawaban Benar: {st.session_state.jawaban_benar} dari 10 soal
    """)
    if st.button("Main Lagi 🔁"):
        st.session_state.halaman = "menu"
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.jawaban_benar = 0
        st.session_state.hint_used = False
