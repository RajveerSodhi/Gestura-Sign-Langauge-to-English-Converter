from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, how are you today?"

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a file
tts.save("output.mp3")

# Playing the converted file on macOS
os.system("open output.mp3")
