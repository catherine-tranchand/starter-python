#Écrire un programme qui demande à l’utilisateur d’entrer un texte
#Le programme devra récupérer ce texte, et l’écrire dans un fichier “output.txt”
#Écrire un programme qui lit le contenu de fichier “output.txt”, et qui l’écrit dans le terminal

texte = input("texte :")
file = open("output.txt", "w")        #"w" - write - pour écrire
file.write(texte)
file.close

file = open("output.txt", "r")
print(file.read())
file.close
