import re

def clean_text(text):
    cleaned_text = text.lower()
    cleaned_text = ' '.join(cleaned_text.split())
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    return cleaned_text


