import streamlit as st

st.set_page_config(page_title="Game Edukasi Mini", layout="centered")

st.title("🎮 Game Edukasi Mini")
st.subheader("Belajar jadi menyenangkan!")

question = "Apa ibu kota Indonesia?"
options = ["Bandung", "Jakarta", "Surabaya"]
answer = "Jakarta"

user_choice = st.radio("Pilih jawaban:", options)

if st.button("Kirim Jawaban"):
    if user_choice == answer:
        st.success("Benar! 🎉")
    else:
        st.error("Salah, coba lagi.")
