from gtts import gTTS
import os



def text_to_speech(text, lang):
    codes = {
        'english':'en',
        'french':'fr',
        'spanish':'es',
        'chinese':'zh-CN',
        'japanese':'ja'
    }
    tts = gTTS(text=text, lang=codes[lang], slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")