myList = [1]
    
    for param in params:
        if isinstance (param, (int)) :
            myList.append(param)
            myList.sort()
        else:
            print ("Attention un des paramètres n'est pas numérique")
            print(myList)

myFunction(3,6,89,78,66,45,2)
