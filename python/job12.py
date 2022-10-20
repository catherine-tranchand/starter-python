import re

f = open("data.txt", "r")
#ouvrir data.txt pour le lire seulement
text = f.read()
pattern = '[a-zA-Z]+'
matches = re.findall("patern", text)