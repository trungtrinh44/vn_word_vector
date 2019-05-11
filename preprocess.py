import unicodedata
import regex


def clean_text(text):
    text = unicodedata.normalize('NFKC', text)
    text = regex.sub(r"[“”]", '"', text)
    text = regex.sub(r"(\w)([[:punct:]]+)(\s)", r"\g<1> \g<2>\g<3>", regex.sub(r"(\s)([[:punct:]]+)(\w)", r"\g<1>\g<2> \g<3>", text))
    text = regex.sub(r"(\w)([[:punct:]]+)", r"\g<1> @\g<2>", regex.sub(r"([[:punct:]]+)(\w)", r"\g<1>@ \g<2>", text))
    text = regex.sub(r"\s+", " ", text)
    return text
