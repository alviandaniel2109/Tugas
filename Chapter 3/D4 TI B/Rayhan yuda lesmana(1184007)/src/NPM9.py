def  NPM9():
    i=0
    NPM = input("Npm : ")
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1
        
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]

    X=1

    for this in A,B,C,D,E,F,G:
    
        if int(this)%2==1:
            print(this,end=" ")
        