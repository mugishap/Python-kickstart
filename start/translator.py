from googletrans import Translator, constants
from pprint import pprint


translator = Translator()
while (True):
    text = input("Enter text to translate or press q to quit: ")
    if text == "q":
        break
    else:
        translation = translator.translate(text,dest='en')
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
