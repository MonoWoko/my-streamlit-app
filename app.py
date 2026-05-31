import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Анализатор текста", page_icon="📊")

st.title("📊 Продвинутый тест: Графики и Файлы")

# 1. Блок загрузки файла
uploaded_file = st.file_uploader("Выберите текстовый файл (.txt)", type="txt")

if uploaded_file is not None:
    # Читаем содержимое
    stringio = uploaded_file.getvalue().decode("utf-8")
    words = stringio.split()
    word_count = len(words)
    
    st.success(f"Файл успешно загружен! Найдено слов: {word_count}")

    # 2. Демонстрация интерактивного графика (Plotly)
    st.subheader("Визуализация случайных данных")
    st.info("Это пример того, как Python рисует графики прямо в браузере.")
    
    # Генерируем простые данные для теста
    data = {"Категория": ["А", "Б", "В", "Г"], "Значение": [word_count, word_count/2, 10, 25]}
    fig = px.bar(data, x="Категория", y="Значение", title="Пример динамического графика", color="Категория")
    
    # Отображаем график в Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Загрузите .txt файл, чтобы увидеть магию Python в действии.")

# 3. Дополнительный интерактив
if st.button('Показать секретное сообщение'):
    st.balloons()
    st.snow()
