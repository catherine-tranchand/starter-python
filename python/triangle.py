#Draw a triangle which will be display by "_", "\", "/"
#In fonction of your input enter which will represent a height of your triangle


left = "/"
right = "\\"
base = "__"

userinput = int(input("height :"))

for i in range(userinput):
    print((userinput - i) * " " + left + ((i * 2) * " ")+ right)
    if i == userinput - 1:
        print(left + base * userinput + right)
        

