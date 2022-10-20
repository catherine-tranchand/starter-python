def myFunction( *params ) :
    myList = [1]

    for param in params:
        if isinstance (param, (int)) :
            myList.append(param)
        else:
            print ("Attention un des paramètres n'est pas numérique")
    
    for element in myList:
        if element % 2 == 0:
            print (element)

myFunction(3,6,89,78,66,8,2)
