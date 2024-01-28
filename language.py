import googletrans
# 3.1.0a0
from googletrans import Translator

def change_language(text, lang):
    translator = Translator()
    out = translator.translate(text, dest=lang)
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
