import streamlit as st
import random
import time

# ----------------- DATA -----------------
unsur_data = [
    {"simbol": "H", "nama": "Hidrogen"},
    {"simbol": "O", "nama": "Oksigen"},
    {"simbol": "Na", "nama": "Natrium"},
    {"simbol": "Cl", "nama": "Klor"},
    {"simbol": "C", "nama": "Karbon"},
    {"simbol": "N", "nama": "Nitrogen"},
    {"simbol": "Fe", "nama": "Besi"},
    {"simbol": "Ca", "nama": "Kalsium"},
    {"simbol": "K", "nama": "Kalium"},
    {"simbol": "Mg", "nama": "Magnesium"}
]

puzzle_data = [
    {"potongan": ["H", "2", "O"], "jawaban": "H2O"},
    {"potongan": ["Na", "Cl"], "jawaban": "NaCl"},
    {"potongan": ["C", "O", "2"], "jawaban": "CO2"},
    {"potongan": ["NH", "3"], "jawaban": "NH3"},
    {"potongan": ["CH", "4"], "jawaban": "CH4"},
    {"potongan": ["H", "2", "SO", "4"], "jawaban": "H2SO4"},
    {"potongan": ["Na", "OH"], "jawaban": "NaOH"},
    {"potongan": ["Ca", "CO", "3"], "jawaban": "CaCO3"},
    {"potongan": ["H", "Cl"], "jawaban": "HCl"},
    {"potongan": ["K", "MnO", "4"], "jawaban": "KMnO4"},
]

bingo_data = [
    {"pertanyaan": "Simbol unsur Natrium?", "jawaban": "Na"},
    {"pertanyaan": "Rumus air?", "jawaban": "H2O"},
    {"pertanyaan": "Rumus garam dapur?", "jawaban": "NaCl"},
    {"pertanyaan": "Rumus karbon dioksida?", "jawaban": "CO2"},
    {"pertanyaan": "Simbol unsur Besi?", "jawaban": "Fe"},
    {"pertanyaan": "Simbol unsur Kalsium?", "jawaban": "Ca"},
    {"pertanyaan": "Rumus amonia?", "jawaban": "NH3"},
    {"pertanyaan": "Simbol unsur Oksigen?", "jawaban": "O"},
    {"pertanyaan": "Simbol unsur Kalium?", "jawaban": "K"},
    {"pertanyaan": "Rumus asam sulfat?", "jawaban": "H2SO4"},
]

# ----------------- SESSION STATE -----------------
if "halaman" not in st.session_state:
    st.session_state.halaman = "menu"
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 0
if "jawaban_benar" not in st.session_state:
    st.session_state.jawaban_benar = 0

# ----------------- HALAMAN -----------------
def halaman_menu():
    st.title("🧪 Chemistry Mini Quiz")
    st.markdown("""
        Pilih mode permainan:
        - **Mode 1**: Tebak nama unsur dari simbol.
        - **Mode 2**: Susun potongan senyawa.
        - **Mode 3**: Bingo istilah dan rumus kimia.
    """)
    if st.button("🔤 Mode 1: Tebak Unsur"):
        st.session_state.halaman = "mode1"
        st.session_state.score = 0
        st.session_state.round = 0
    elif st.button("🧩 Mode 2: Puzzle Senyawa"):
        st.session_state.halaman = "mode2"
        st.session_state.score = 0
        st.session_state.round = 0
    elif st.button("🎯 Mode 3: Bingo Kimia"):
        st.session_state.halaman = "mode3"
        st.session_state.score = 0
        st.session_state.round = 0

# ----------------- MODE 1 -----------------
def halaman_mode1():
    st.subheader(f"Babak {st.session_state.round + 1} dari 10")
    soal = random.choice(unsur_data)
    opsi = random.sample([x["nama"] for x in unsur_data if x["nama"] != soal["nama"]], 3)
    opsi.append(soal["nama"])
    random.shuffle(opsi)

    st.markdown(f"**Simbol: {soal['simbol']}**")
    jawaban = st.radio("Pilih nama unsur:", opsi, key=f"radio1_{st.session_state.round}")

    if st.button("Kirim Jawaban"):
        if jawaban == soal["nama"]:
            st.success("Jawaban benar!")
            st.session_state.score += 10
            st.session_state.jawaban_benar += 1
        else:
            st.error(f"Salah. Jawaban benar: {soal['nama']}")
        st.session_state.round += 1

    if st.session_state.round >= 10:
        st.session_state.halaman = "hasil"

# ----------------- MODE 2 -----------------
def halaman_mode2():
    st.subheader(f"Babak {st.session_state.round + 1} dari 10")
    soal = puzzle_data[st.session_state.round]
    potongan = soal["potongan"]
    st.markdown("Susun potongan berikut menjadi satu rumus senyawa yang benar:")
    st.markdown(" + ".join(potongan))

    jawaban = st.text_input("Masukkan rumus senyawa lengkap (contoh: H2O):", key=f"puzzle_{st.session_state.round}")

    if st.button("Kirim Jawaban"):
        if jawaban.strip() == soal["jawaban"]:
            st.success("Jawaban benar!")
            st.session_state.score += 10
            st.session_state.jawaban_benar += 1
        else:
            st.error(f"Jawaban salah. Benar: {soal['jawaban']}")
        st.session_state.round += 1

    if st.session_state.round >= 10:
        st.session_state.halaman = "hasil"

# ----------------- MODE 3 -----------------
def halaman_mode3():
    st.subheader(f"Babak {st.session_state.round + 1} dari 10")
    soal = bingo_data[st.session_state.round]
    st.markdown(f"❓ {soal['pertanyaan']}")
    jawaban = st.text_input("Jawaban kamu:", key=f"bingo_{st.session_state.round}")

    if st.button("Kirim Jawaban"):
        if jawaban.strip() == soal["jawaban"]:
            st.success("Benar!")
            st.session_state.score += 10
            st.session_state.jawaban_benar += 1
        else:
            st.error(f"Jawaban salah. Benar: {soal['jawaban']}")
        st.session_state.round += 1

    if st.session_state.round >= 10:
        st.session_state.halaman = "hasil"

# ----------------- HASIL -----------------
def halaman_hasil():
    st.balloons()
    st.title("🎉 Permainan Selesai!")
    st.markdown(f"**Skor Akhir: {st.session_state.score} dari 100**")
    st.markdown(f"✅ Jawaban benar: {st.session_state.jawaban_benar} dari 10")
    st.markdown("---")
    if st.button("🔁 Main Lagi"):
        st.session_state.halaman = "menu"
        st.session_state.score = 0
        st.session_state.round = 0
        st.session_state.jawaban_benar = 0

# ----------------- ROUTING -----------------
if st.session_state.halaman == "menu":
    halaman_menu()
elif st.session_state.halaman == "mode1":
    halaman_mode1()
elif st.session_state.halaman == "mode2":
    halaman_mode2()
elif st.session_state.halaman == "mode3":
    halaman_mode3()
elif st.session_state.halaman == "hasil":
    halaman_hasil()
