import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from analyzer.language import detect_language
from analyzer.frequency import remove_stopwords
from analyzer.utils import clean_text


def count_words(text):

    language = detect_language(text)

    cleaned = remove_stopwords(text)

    cleaned = ' '.join(cleaned)


    if language == 'ru':
        tokens = word_tokenize(cleaned, language='russian')

    elif language == 'en':
        tokens = word_tokenize(cleaned, language='english')

    words = [word for word in tokens if word.isalnum()]
    word_count = len(words)

    return word_count


def count_sentences(text):

    language = detect_language(text)

    if language == 'ru':
        sentences = sent_tokenize(text, 'russian')
        return len(sentences)
    elif language == 'en':
        sentences = sent_tokenize(text, 'english')
        return len(sentences)

    return  None


def count_characters(text):

    cleaned = clean_text(text)
    cleaned = cleaned.split(' ')
    cleaned = ''.join(cleaned)

    return len(cleaned)


def average_word_length(text):

    amount = count_words(text)
    length = count_characters(text)

    mean = length / amount

    return round(mean, 2)