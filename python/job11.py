#Créer un programme qui parcourt le contenu du fichier “domains.xml” 
#Le programme qui compte le nombre de noms de domaine
#https: //pythonforge

from xml.dom import minidom
doc = minidom.parse('domains.xlm')
elements = doc.getElementsByTagName("column")
newList = []
for element in elements:
    if element .getAttribute("name") == "domain":
        newList.append(element.chilNodes[0].data)

print(len("newList"))