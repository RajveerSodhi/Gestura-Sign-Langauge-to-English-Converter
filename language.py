import googletrans
# 3.1.0a0
from googletrans import Translator

def change_language(text, lang):
    codes = {
    "afrikaans": "af",
  "albanian": "sq",
  "amharic": "am",
  "arabic": "ar",
  "armenian": "hy",
  "azerbaijani": "az",
  "basque": "eu",
  "belarusian": "be",
  "bengali": "bn",
  "bosnian": "bs",
  "bulgarian": "bg",
  "catalan": "ca",
  "cebuano": "ceb",
  "chichewa": "ny",
  "chinese (simplified)": "zh",
  "chinese (traditional)": "zh-tw",
  "corsican": "co",
  "croatian": "hr",
  "czech": "cs",
  "danish": "da",
  "dutch": "nl",
  "english": "en",
  "esperanto": "eo",
  "estonian": "et",
  "filipino": "tl",
  "finnish": "fi",
  "french": "fr",
  "frisian": "fy",
  "galician": "gl",
  "georgian": "ka",
  "german": "de",
  "greek": "el",
  "gujarati": "gu",
  "haitian creole": "ht",
  "hausa": "ha",
  "hawaiian": "haw",
  "hebrew": "he",
  "hindi": "hi",
  "hmong": "hmn",
  "hungarian": "hu",
  "icelandic": "is",
  "igbo": "ig",
  "indonesian": "id",
  "irish": "ga",
  "italian": "it",
  "japanese": "ja",
  "javanese": "jw",
  "kannada": "kn",
  "kazakh": "kk",
  "khmer": "km",
  "korean": "ko",
  "kurdish (kurmanji)": "ku",
  "kyrgyz": "ky",
  "lao": "lo",
  "latin": "la",
  "latvian": "lv",
  "lithuanian": "lt",
  "luxembourgish": "lb",
  "macedonian": "mk",
  "malagasy": "mg",
  "malay": "ms",
  "malayalam": "ml",
  "maltese": "mt",
  "maori": "mi",
  "marathi": "mr",
  "mongolian": "mn",
  "myanmar (burmese)": "my",
  "nepali": "ne",
  "norwegian": "no",
  "pashto": "ps",
  "persian": "fa",
  "polish": "pl",
  "portuguese": "pt",
  "punjabi": "pa",
  "romanian": "ro",
  "russian": "ru",
  "samoan": "sm",
  "scots gaelic": "gd",
  "serbian": "sr",
  "sesotho": "st",
  "shona": "sn",
  "sindhi": "sd",
  "sinhala": "si",
  "slovak": "sk",
  "slovenian": "sl",
  "somali": "so",
  "spanish": "es",
  "sundanese": "su",
  "swahili": "sw",
  "swedish": "sv",
  "tajik": "tg",
  "tamil": "ta",
  "telugu": "te",
  "thai": "th",
  "turkish": "tr",
  "ukrainian": "uk",
  "urdu": "ur",
  "uzbek": "uz",
  "vietnamese": "vi",
  "welsh": "cy",
  "xhosa": "xh",
  "yiddish": "yi",
  "yoruba": "yo",
  "zulu": "zu",
    }

    translator = Translator()
    out = translator.translate(text, dest=codes[lang])
    return out.text

# text = '''How are you doing'''
#
# translator = Translator()
#
# # French
# out = translator.translate(text, dest="fr")
# print(out.text)
# # Spanish
# out = translator.translate(text, dest="es")
# print(out.text)
# # Chinese
# out = translator.translate(text, dest="zh-CN")
# print(out.text)
# # Japanese
# out = translator.translate(text, dest="ja")
# print(out.text)