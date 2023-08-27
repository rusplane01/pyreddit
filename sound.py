from gtts import gTTS 
from playsound import playsound

#text_val = 'спасибо что посетили наш сайт. наша служба поддержки +359 029 582 206'

text_val = '*%*'

language = 'bg'

obj = gTTS(text=text_val, lang=language, slow=False)


obj.save("test.mp3")
playsound("test.mp3")