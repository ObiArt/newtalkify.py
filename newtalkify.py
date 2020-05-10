from googletrans import Translator
import sys, random
translator = Translator()

if (len(sys.argv) <= 1):
    raise Exception("No parameters were given!")

print("Opening file...")
file = open(sys.argv[1],"r",encoding='utf-8')
text = file.read()
file.close()
print("File opened!")
newtext = ""
for line in text.split("\n"):
    for word in line.split():
        if random.random() < 0.25:
            word = translator.translate(word, dest="en").text
            print("Translating...")
        newtext += word + " "
    newtext += "\n"
print("Translation complete!")
print("Writing new file...")
file = open(sys.argv[1],"w",encoding='utf-8')
file.write(newtext)
file.close()
print("Done!")
