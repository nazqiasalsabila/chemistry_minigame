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
    try:
        banner = Image.open("assets/banner.png")
        st.image(banner, use_container_width=True)
    except:
        st.warning("Gambar banner tidak ditemukan. Letakkan banner.png di folder assets.")

    st.markdown("<h1 style='text-align:center;'>🎮 Periodic Table Quiz</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;'>
        <p>Tebak nama unsur dari simbol kimia!</p>
        <p>🔸 10 babak | ⏱️ 30 detik per babak | 💯 Total skor: 100</p>
        <p>💡 Hint tersedia 1x per game</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Mulai Quiz 🚀"):
        st.session_state.halaman = "quiz"
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.hint_used = False
        st.session_state.soal_sekarang = None
        st.session_state.start_time = time.time()
        st.rerun()

# ---------- HALAMAN QUIZ ----------
def halaman_quiz():
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

    st.markdown(f"**Simbol Unsur:** `{soal['simbol']}`")

    if not st.session_state.hint_used and st.button("Gunakan Hint 💡"):
        huruf_awal = soal["jawaban_benar"][0]
        st.info(f"Clue: Nama unsur diawali huruf **{huruf_awal}**")
        st.session_state.hint_used = True

    pilihan = st.radio("Pilih jawaban:", soal["opsi"])

    waktu_berjalan = int(time.time() - st.session_state.start_time)
    sisa_waktu = max(0, 30 - waktu_berjalan)
    progress = sisa_waktu / 30.0
    st.progress(1 - progress)
    st.info(f"⏳ Sisa waktu: {sisa_waktu} detik")

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

# ---------- HALAMAN SKOR ----------
def halaman_skor():
    st.markdown("## 🏁 Quiz Selesai!")
    st.success(f"Skor Akhir Kamu: {st.session_state.score} dari 100 🎉")

    if st.session_state.score == 100:
        st.balloons()
    elif st.session_state.score >= 70:
        st.markdown("🎉 Keren! Kamu paham kimia dengan baik!")
    else:
        st.markdown("📘 Yuk belajar lagi, kamu pasti bisa!")

    if st.button("Main Lagi 🔄"):
        st.session_state.halaman = "mulai"
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.hint_used = False
        st.session_state.soal_sekarang = None
        st.rerun()

# ---------- NAVIGASI ----------
if st.session_state.halaman == "mulai":
    halaman_mulai()
elif st.session_state.halaman == "quiz":
    halaman_quiz()
elif st.session_state.halaman == "skor":
    halaman_skor()
