import streamlit as st

# Judul Aplikasi
st.set_page_config(page_title="Simulasi Bahaya Bahan Kimia", page_icon="🧯", layout="centered")
st.title("🧪 Simulasi Bahaya Bahan Kimia")
st.markdown("Cocok untuk edukasi **K3 Laboratorium**. Pilih bahan kimia dan lihat informasi bahayanya!")

# Data bahan kimia (Contoh sederhana)
bahan_kimia = {
    "Asam Sulfat (H₂SO₄)": {
        "piktogram": ["corrosive.png", "exclamation.png"],
        "risiko": ["Korosif", "Iritasi saluran pernapasan", "Bahaya kulit & mata"],
        "penanganan": "Gunakan APD lengkap. Tambahkan ke air, jangan sebaliknya. Hindari kontak langsung.",
        "apd": ["Sarung tangan tahan asam", "Kacamata safety", "Jas lab", "Masker"]
    },
    "Amonia (NH₃)": {
        "piktogram": ["gas.png", "exclamation.png"],
        "risiko": ["Toksik jika terhirup", "Iritasi mata & kulit", "Korosif"],
        "penanganan": "Gunakan di ruang berventilasi. Hindari menghirup uap. Simpan dalam suhu rendah.",
        "apd": ["Masker gas", "Kacamata safety", "Sarung tangan nitril"]
    },
    "Aseton (C₃H₆O)": {
        "piktogram": ["flammable.png", "exclamation.png"],
        "risiko": ["Mudah terbakar", "Iritasi mata", "Efek anestetik"],
        "penanganan": "Jauhkan dari sumber panas. Tutup rapat. Gunakan di ruang berventilasi.",
        "apd": ["Masker uap organik", "Sarung tangan nitril", "Kacamata"]
    },
}

# Pilih bahan kimia
pilihan = st.selectbox("🔍 Pilih Bahan Kimia:", list(bahan_kimia.keys()))

data = bahan_kimia[pilihan]

# Tampilkan piktogram
st.subheader("📛 Piktogram Bahaya (GHS)")
cols = st.columns(len(data["piktogram"]))
for i, gambar in enumerate(data["piktogram"]):
    with cols[i]:
        st.image(f"piktogram/{gambar}", width=100)

# Tampilkan risiko
st.subheader("⚠️ Risiko")
for risiko in data["risiko"]:
    st.markdown(f"- {risiko}")

# Tampilkan cara penanganan
st.subheader("🛠️ Cara Penanganan")
st.markdown(data["penanganan"])

# Tampilkan APD
st.subheader("🧤 Alat Pelindung Diri (APD)")
for apd in data["apd"]:
    st.markdown(f"- {apd}")

# Footer
st.markdown("---")
st.markdown("🧯 *Aplikasi edukasi K3 laboratorium berbasis GHS oleh Streamlit.io*")

