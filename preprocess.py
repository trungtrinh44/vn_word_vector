import unicodedata
import regex


def clean_text(text, lower=False):
    text = unicodedata.normalize('NFKC', text)
    text = regex.sub(r"[“”]", '"', text)
    text = regex.sub(r"([[:punct:]])", r" \g<1> ", text)
    text = regex.sub(r"\s+", " ", text)
    if lower:
        return text.lower()
    return text
