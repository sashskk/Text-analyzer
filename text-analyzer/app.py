import streamlit as st
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from analyzer.language import detect_language
from analyzer.text_stats import count_words, count_sentences, count_characters, average_word_length
from analyzer.utils import clean_text
from analyzer.frequency import get_top_words, count_frequency


def load_text(uploaded_file):
    return uploaded_file.getvalue().decode('utf-8')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

st.title('Анализатор текста')
uploaded_file = st.file_uploader('Загрузите TXT Файл', type=['txt'])

st.divider()

if uploaded_file is not None:
    text = load_text(uploaded_file)

    language = detect_language(text)
    cleaned_text = clean_text(text)

    word_count = count_words(cleaned_text)
    sentences_count = count_sentences(text)
    characters_count = count_characters(text)
    average_length = average_word_length(text) # не учитывает stopwords

    words_frequency = count_frequency(text)
    top_words = get_top_words(cleaned_text)

    col1, col2, col3 = st.columns(3)

    st.subheader('📊 Статистика:')
    with col1:
        st.metric(label='Кол-во Слов', value=word_count)
    with col2:
        st.metric(label='Всего Предложений', value=sentences_count)
    with col3:
        st.metric(label='Кол-во букв', value=characters_count)

    if language == 'ru':
        st.write('Язык: ', 'Русский')
    elif language == 'en':
        st.write('Язык: ', 'Английский')
    st.write('Средняя длина слов:', average_length)

    st.divider()

    st.subheader('🚀 Топ 10 Слов:')
    for word, num in top_words:
        st.write(f'{word}: {num}')

    st.divider()

    st.subheader('🔥 Облако слов')

    try:
        cloud = WordCloud(
            width=1000,
            height=500,
            background_color='white',
            font_path='C:/Windows/Fonts/arial.ttf'
        ).generate(cleaned_text)

        fig, ax = plt.subplots(
            figsize=(10,5)
        )

        ax.imshow(cloud)

        ax.axis('off')

        st.pyplot(fig)

    except Exception as e:
        st.error(
            f'Ошибка построения облака: {e}'
        )

