# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
speech = 'There are several APIs available to convert text to speech in python'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
play = gTTS(text=speech, lang=language, slow=False)

# play.save("file.mp3")
#
# Saving the converted audio in a mp3 file named file.mp3
# os.system("start file.mp3")

file = open('mytile.txt', 'r').read().replace("\n", ' ')

audio_file = gTTS(text=str(file), lang=language, slow=False)

audio_file.save("myfile.mp3")
os.system('start myfile.mp3')