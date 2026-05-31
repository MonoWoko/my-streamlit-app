import streamlit as st

st.title("🚀 Мое первое веб-приложение")
st.write("Это приложение работает прямо из облака!")

number = st.slider("Выберите число", 0, 100, 50)
st.write(f"Квадрат числа {number} равен {number**2}")
