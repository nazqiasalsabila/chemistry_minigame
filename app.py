# chemistry_quiz_game/app.py
import streamlit as st
from PIL import Image
import time
import random

# ---------- DATA MODE 1: TEBAK UNSUR ----------
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

# ---------- DATA MODE 2: PUZZLE STRUKTUR (Sederhana) ----------
puzzle_data = [
    {"gambar": "assets/puzzle1.png", "nama": "H2O"},
    {"gambar": "assets/puzzle2.png", "nama": "CO2"},
    {"gambar": "assets/puzzle3.png", "nama": "CH4"},
    {"gambar": "assets/puzzle4.png", "nama": "NH3"},
    {"gambar": "assets/puzzle5.png", "nama": "NaCl"},
    {"gambar": "assets/puzzle6.png", "nama": "C2H5OH"},
    {"gambar": "assets/puzzle7.png", "nama": "C6H12O6"},
    {"gambar": "assets/puzzle8.png", "nama": "H2SO4"},
    {"gambar": "assets/puzzle9.png", "nama": "CaCO3"},
    {"gambar": "assets/puzzle10.png", "nama": "KNO3"},
]

# ---------- DATA MODE 3: BINGO KIMIA ----------
bingo_data = [
    {"istilah": "Mol", "definisi": "Satuan jumlah zat"},
    {"istilah": "Hukum Avogadro", "definisi": "V ∝ n (tekanan dan suhu tetap)"},
    {"istilah": "Ion", "definisi": "Atom bermuatan"},
    {"istilah": "Isotop", "definisi": "Atom dengan neutron berbeda"},
    {"istilah": "Reaksi Redoks", "definisi": "Reaksi reduksi dan oksidasi"},
    {"istilah": "pH", "definisi": "Ukuran keasaman"},
    {"istilah": "Ikatan Kovalen", "definisi": "Berbagi pasangan elektron"},
    {"istilah": "Ikatan Ionik", "definisi": "Transfer elektron"},
    {"istilah": "Katalis", "definisi": "Mempercepat reaksi tanpa ikut bereaksi"},
    {"istilah": "Hidrokarbon", "definisi": "Senyawa karbon dan hidrogen saja"},
]

# ---------- INISIALISASI SESSION ----------
if "mode" not in st.session_state:
    st.session_state.mode = None
if "halaman" not in st.session_state:
    st.session_state.halaman = "menu"
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "soal_sekarang" not in st.session_state:
    st.session_state.soal_sekarang = None
if "hint_used" not in st.session_state:
    st.session_state.hint_used = False

# ---------- HALAMAN MENU UTAMA ----------
def halaman_menu():
    st.markdown("""
        <h1 style='text-align:center;'>🧪 Chemistry Quiz Games</h1>
        <p style='text-align:center;'>Pilih mode permainan:</p>
    """, unsafe_allow_html=True)

    mode = st.selectbox("Mode Permainan:", ["Tebak Unsur", "Puzzle Senyawa", "Kartu Bingo"])
    if st.button("Mulai Permainan 🚀"):
        st.session_state.mode = mode
        st.session_state.halaman = "quiz"
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.soal_sekarang = None
        st.session_state.hint_used = False
        st.rerun()

# ---------- HALAMAN QUIZ TEBak UNSUR ----------
def halaman_tebak_unsur():
    st.markdown(f"### 🔢 Babak {st.session_state.round} dari 10")

    if not st.session_state.soal_sekarang:
        soal = random.choice(unsur_data)
        jawaban_benar = soal["nama"]
        opsi = [jawaban_benar]
        while len(opsi) < 4:
            pilihan = random.choice(unsur_data)["nama"]
            if pilihan not in opsi:
                opsi.append(pilihan)
        random.shuffle(opsi)
        st.session_state.soal_sekarang = {
            "simbol": soal["simbol"],
            "jawaban_benar": jawaban_benar,
            "opsi": opsi,
        }
        st.session_state.start_time = time.time()

    soal = st.session_state.soal_sekarang
    st.markdown(f"<h2 style='text-align:center;'>Simbol: {soal['simbol']}</h2>", unsafe_allow_html=True)

    if not st.session_state.hint_used and st.button("Gunakan Hint 💡"):
        huruf_awal = soal["jawaban_benar"][0]
        st.info(f"Clue: Nama unsur diawali huruf **{huruf_awal}**")
        st.session_state.hint_used = True

    pilihan = st.radio("Pilih jawaban:", soal["opsi"], index=None)

    waktu_berjalan = int(time.time() - st.session_state.start_time)
    sisa_waktu = max(0, 30 - waktu_berjalan)
    st.progress((30 - sisa_waktu)/30)
    st.caption(f"⏱️ Sisa waktu: {sisa_waktu} detik")

    if sisa_waktu == 0 or st.button("Kirim Jawaban"):
        if pilihan == soal["jawaban_benar"]:
            st.success("✅ Jawaban Benar!")
            st.markdown("<audio autoplay><source src='assets/correct.mp3' type='audio/mpeg'></audio>", unsafe_allow_html=True)
            st.session_state.score += 10
        else:
            st.error(f"❌ Salah! Jawaban benar: {soal['jawaban_benar']}")
            st.markdown("<audio autoplay><source src='assets/wrong.mp3' type='audio/mpeg'></audio>", unsafe_allow_html=True)

        if st.session_state.round < 10:
            st.session_state.round += 1
            st.session_state.soal_sekarang = None
            st.rerun()
        else:
            st.session_state.halaman = "skor"
            st.rerun()

# ---------- HALAMAN QUIZ PUZZLE ----------
def halaman_puzzle():
    st.markdown(f"### 🧩 Babak {st.session_state.round} dari 10")
    soal = puzzle_data[st.session_state.round - 1]
    st.image(soal["gambar"], use_container_width=True)
    pilihan = st.text_input("Masukkan nama senyawa berdasarkan gambar di atas:")

    if st.button("Kirim Jawaban"):
        if pilihan.strip().upper() == soal["nama"].upper():
            st.success("✅ Benar!")
            st.markdown("<audio autoplay><source src='assets/correct.mp3' type='audio/mpeg'></audio>", unsafe_allow_html=True)
            st.session_state.score += 10
        else:
            st.error(f"❌ Salah! Jawaban: {soal['nama']}")
            st.markdown("<audio autoplay><source src='assets/wrong.mp3' type='audio/mpeg'></audio>", unsafe_allow_html=True)

        if st.session_state.round < 10:
            st.session_state.round += 1
            st.rerun()
        else:
            st.session_state.halaman = "skor"
            st.rerun()

# ---------- HALAMAN QUIZ BINGO ----------
def halaman_bingo():
    st.markdown(f"### 🧠 Babak {st.session_state.round} dari 10")
    soal = bingo_data[st.session_state.round - 1]
    st.info(f"Istilah: {soal['istilah']}")
    pilihan = st.text_area("Tulis definisi istilah di atas:")

    if st.button("Kirim Jawaban"):
        if soal["definisi"].lower() in pilihan.lower():
            st.success("✅ Definisi sesuai!")
            st.markdown("<audio autoplay><source src='assets/correct.mp3' type='audio/mpeg'></audio>", unsafe_allow_html=True)
            st.session_state.score += 10
        else:
            st.error(f"❌ Kurang tepat. Definisi: {soal['definisi']}")
            st.markdown("<audio autoplay><source src='assets/wrong.mp3' type='audio/mpeg'></audio>", unsafe_allow_html=True)

        if st.session_state.round < 10:
            st.session_state.round += 1
            st.rerun()
        else:
            st.session_state.halaman = "skor"
            st.rerun()

# ---------- HALAMAN SKOR ----------
def halaman_skor():
    st.markdown("## 🏁 Quiz Selesai!")
    st.success(f"Skor Akhir Kamu: {st.session_state.score} dari 100 🎉")

    if st.button("Main Lagi 🔁"):
        st.session_state.halaman = "menu"
        st.session_state.mode = None
        st.session_state.round = 1
        st.session_state.score = 0
        st.session_state.soal_sekarang = None
        st.session_state.hint_used = False
        st.rerun()

# ---------- ROUTING ----------
if st.session_state.halaman == "menu":
    halaman_menu()
elif st.session_state.halaman == "quiz":
    if st.session_state.mode == "Tebak Unsur":
        halaman_tebak_unsur()
    elif st.session_state.mode == "Puzzle Senyawa":
        halaman_puzzle()
    elif st.session_state.mode == "Kartu Bingo":
        halaman_bingo()
elif st.session_state.halaman == "skor":
    halaman_skor()
