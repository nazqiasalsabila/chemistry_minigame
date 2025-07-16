import streamlit as st
import random
import time

# ---------------------------- DATA ----------------------------
data_unsur = [
    {"simbol": "H", "nama": "Hidrogen"},
    {"simbol": "O", "nama": "Oksigen"},
    {"simbol": "N", "nama": "Nitrogen"},
    {"simbol": "C", "nama": "Karbon"},
    {"simbol": "Na", "nama": "Natrium"},
    {"simbol": "Cl", "nama": "Klor"},
    {"simbol": "Fe", "nama": "Besi"},
    {"simbol": "Ca", "nama": "Kalsium"},
    {"simbol": "K", "nama": "Kalium"},
    {"simbol": "Mg", "nama": "Magnesium"},
]

soal_puzzle = [
    {"potongan": ["H", "2", "O"], "jawaban": "H2O"},
    {"potongan": ["C", "O", "2"], "jawaban": "CO2"},
    {"potongan": ["N", "H", "3"], "jawaban": "NH3"},
    {"potongan": ["C", "H", "4"], "jawaban": "CH4"},
    {"potongan": ["H", "2", "S"], "jawaban": "H2S"},
]

soal_bingo = [
    {"istilah": "H2O", "deskripsi": "Senyawa air"},
    {"istilah": "CO2", "deskripsi": "Gas rumah kaca"},
    {"istilah": "NaCl", "deskripsi": "Garam dapur"},
    {"istilah": "CH4", "deskripsi": "Gas metana"},
    {"istilah": "NH3", "deskripsi": "Amonia"},
]

# ---------------------------- STATE ----------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "menu"
if "soal_index" not in st.session_state:
    st.session_state.soal_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------------------- FUNCTIONS ----------------------------
def reset_game():
    st.session_state.soal_index = 0
    st.session_state.score = 0

def menu():
    st.title("🧪 Chemistry Mini Games")
    st.write("Pilih mode permainan:")
    if st.button("1️⃣ Tebak Unsur dari Simbol"):
        reset_game()
        st.session_state.mode = "game1"
    if st.button("2️⃣ Susun Potongan Senyawa"):
        reset_game()
        st.session_state.mode = "game2"
    if st.button("3️⃣ Kartu Bingo Kimia"):
        reset_game()
        st.session_state.mode = "game3"

def game1():
    soal = random.choice(data_unsur)
    pilihan = random.sample(data_unsur, 3)
    if soal not in pilihan:
        pilihan[random.randint(0,2)] = soal
    st.subheader(f"Babak {st.session_state.soal_index+1} dari 10")
    st.markdown(f"### Apa nama unsur dari simbol **{soal['simbol']}**?")
    jawaban = st.radio("Pilih jawaban:", [p["nama"] for p in pilihan])

    if st.button("Jawab"):
        if jawaban == soal["nama"]:
            st.success("Benar!")
            st.session_state.score += 10
        else:
            st.error(f"Salah. Jawaban: {soal['nama']}")

        next_soal()

def game2():
    soal = soal_puzzle[st.session_state.soal_index % len(soal_puzzle)]
    st.subheader(f"Babak {st.session_state.soal_index+1} dari 10")
    st.markdown("### Susun potongan berikut menjadi senyawa yang benar:")
    st.write(" + ".join(soal["potongan"]))

    pilihan = [soal["jawaban"], "HO2", "H2", "OH2"]
    random.shuffle(pilihan)
    jawaban = st.radio("Pilih senyawa:", pilihan)

    if st.button("Jawab"):
        if jawaban == soal["jawaban"]:
            st.success("Benar!")
            st.session_state.score += 10
        else:
            st.error(f"Salah. Jawaban: {soal['jawaban']}")
        next_soal()

def game3():
    soal = soal_bingo[st.session_state.soal_index % len(soal_bingo)]
    st.subheader(f"Babak {st.session_state.soal_index+1} dari 10")
    st.markdown(f"### {soal['deskripsi']}")

    pilihan = [soal["istilah"], "H2", "C6H12O6", "Na2SO4"]
    random.shuffle(pilihan)
    jawaban = st.radio("Pilih istilah/rumus yang sesuai:", pilihan)

    if st.button("Jawab"):
        if jawaban == soal["istilah"]:
            st.success("Benar!")
            st.session_state.score += 10
        else:
            st.error(f"Salah. Jawaban: {soal['istilah']}")
        next_soal()

def next_soal():
    time.sleep(1)
    st.session_state.soal_index += 1
    if st.session_state.soal_index >= 10:
        st.session_state.mode = "hasil"
    else:
        st.experimental_rerun()

def hasil():
    st.title("🏁 Permainan Selesai!")
    st.write(f"Skor akhir kamu: **{st.session_state.score} / 100**")
    if st.button("Kembali ke Menu"):
        st.session_state.mode = "menu"

# ---------------------------- ROUTER ----------------------------
if st.session_state.mode == "menu":
    menu()
elif st.session_state.mode == "game1":
    game1()
elif st.session_state.mode == "game2":
    game2()
elif st.session_state.mode == "game3":
    game3()
elif st.session_state.mode == "hasil":
    hasil()
