# This project translate any of the language, it's like a google translator
# This project contains module name translate, download it first and run the program
# and from_lang and to_lang in-build function is used

from translate import Translator
data = input("Enter something to translate:- ")
Hindi = Translator(from_lang="English", to_lang="Hindi")
arabic = Translator(from_lang="English", to_lang="Arabic")
print(Hindi.translate(data))
print(arabic.translate(data))
