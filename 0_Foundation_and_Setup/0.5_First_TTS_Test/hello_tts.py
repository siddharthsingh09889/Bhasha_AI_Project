from gtts import gTTS
import os

text = "Hello Siddharth! Welcome to your first AI voice test."
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")

# For macOS
os.system("open hello.mp3")
