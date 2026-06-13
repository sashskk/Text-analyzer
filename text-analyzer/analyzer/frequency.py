import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from collections import Counter
from analyzer.utils import clean_text

from analyzer.language import detect_language


# nltk.download('punkt')
# nltk.download('stopwords')


def get_top_words(text):
    cleaned = clean_text(text)
    cleaned = remove_stopwords(cleaned)
    top_words = Counter(cleaned)
    return top_words.most_common(10)


def remove_stopwords(text):
    language = detect_language(text)

    cleaned_text = clean_text(text)

    if language == 'ru':
        words = word_tokenize(cleaned_text, 'russian')
        stop_words = set(stopwords.words('russian'))
        filtered_text = [word for word in words if word.lower() not in stop_words]
        return filtered_text

    elif language == 'en':
        words = word_tokenize(cleaned_text, 'english')
        stop_words = set(stopwords.words('english'))
        filtered_text = [word for word in words if word.lower() not in stop_words]
        return filtered_text

    return None


def count_frequency(text):
    filtered_text = remove_stopwords(text)
    counts = Counter(filtered_text)
    return counts


