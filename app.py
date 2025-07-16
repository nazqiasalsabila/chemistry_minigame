import streamlit as st
import random
import time

st.set_page_config(page_title="Periodic Table Quiz", layout="centered")

# Data unsur kimia
data_unsur = [
    {"simbol": "H", "nama": "Hidrogen", "no_atom": 1, "senyawa": "H2O"},
    {"simbol": "O", "nama": "Oksigen", "no_atom": 8, "senyawa": "CO2"},
    {"simbol": "Na", "nama": "Natrium", "no_atom": 11, "senyawa": "NaCl"},
    {"simbol": "Cl", "nama": "Klorin", "no_atom": 17, "senyawa": "HCl"},
    {"simbol": "C", "nama": "Karbon", "no_atom": 6, "senyawa": "CH4"},
    {"simbol": "Fe", "nama": "Besi", "no_atom": 26, "senyawa": "Fe2O3"},
    {"simbol": "Au", "nama": "Emas", "no_atom": 79, "senyawa": "-"},
    {"simbol": "Ag", "nama": "Perak", "no_atom": 47, "senyawa": "-"},
    {"simbol": "N", "nama": "Nitrogen", "no_atom": 7, "senyawa": "NH3"},
    {"simbol": "K", "nama": "Kalium", "no_atom": 19, "senyawa": "KCl"},
]

# --- Navigasi ---
menu = st.sidebar.selectbox("📚 Pilih Halaman", ["🏠 Beranda", "🧪 Mulai Kuis"])

# --- Beranda ---
if menu == "🏠 Beranda":
    st.image("assets/banner.png", use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>🧪 Periodic Table Quiz</h1>", unsafe_allow_html=True)
    st.markdown("""
    Selamat datang di **Periodic Table Quiz**!
    
    🎯 **Deskripsi Game**:  
    Tebak nama unsur berdasarkan:
    - Simbol unsur (contoh: 'Na')
    - Nomor atom
    - Senyawa terkenal
    
    🕐 **Fitur Seru**:  
    - Mode cepat (60 detik total)  
    - Hint tersedia 1 kali per game  
    - 10 pertanyaan acak  
    - Skor akhir ditampilkan
    """)
    st.success("Klik menu '🧪 Mulai Kuis' di kiri untuk bermain!")

# --- Game Kuis ---
elif menu == "🧪 Mulai Kuis":
    st.title("🧪 Periodic Table Quiz")

    # Simpan state di session_state
    if "soal_ke" not in st.session_state:
        st.session_state.soal_ke = 0
        st.session_state.score = 0
        st.session_state.mulai_waktu = time.time()
        st.session_state.hint_dipakai = False
        random.shuffle(data_unsur)
    
    # Timer
    waktu_berjalan = int(time.time() - st.session_state.mulai_waktu)
    sisa_waktu = 60 - waktu_berjalan
    st.warning(f"⏰ Sisa waktu: {sisa_waktu} detik")

    if sisa_waktu <= 0:
        st.error("⛔ Waktu habis!")
        st.write(f"🎯 Skor akhir: **{st.session_state.score} / 10**")
        st.button("🔄 Coba Lagi", on_click=lambda: st.session_state.clear())

    elif st.session_state.soal_ke < 10:
        # Ambil soal saat ini
        soal = data_unsur[st.session_state.soal_ke]
        mode_soal = random.choice(["simbol", "no_atom", "senyawa"])

        if mode_soal == "simbol":
            pertanyaan = f"🌟 Unsur dengan simbol **{soal['simbol']}** adalah..."
        elif mode_soal == "no_atom":
            pertanyaan = f"🔢 Unsur dengan nomor atom **{soal['no_atom']}** adalah..."
        else:
            pertanyaan = f"🧪 Unsur yang membentuk senyawa **{soal['senyawa']}** adalah..."

        st.subheader(f"Babak {st.session_state.soal_ke + 1} / 10")
        st.write(pertanyaan)
        jawaban = st.text_input("Tulis nama unsur (huruf kecil boleh):")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✅ Jawab"):
                if jawaban.strip().lower() == soal["nama"].lower():
                    st.success("Benar! 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"Salah! Jawaban: **{soal['nama']}**")
                st.session_state.soal_ke += 1
                st.rerun()

        with col2:
            if st.button("💡 Gunakan Hint", disabled=st.session_state.hint_dipakai):
                st.session_state.hint_dipakai = True
                st.info(f"Hint: Unsur ini memiliki simbol **{soal['simbol']}** dan nomor atom **{soal['no_atom']}**")

    else:
        st.success("✅ Kuis selesai!")
        st.metric("🎯 Skor Akhir", f"{st.session_state.score} / 10")
        st.button("🔄 Main Lagi", on_click=lambda: st.session_state.clear())
