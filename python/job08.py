height = int(input("height :"))
width = int(input("width :"))
side = "|"
separateur = "-"

for i in range(height):
    if i == 0 or i == height -1:
        separateur = "-"
    else:
        separateur = " "
    print(side +separateur * width + side)







