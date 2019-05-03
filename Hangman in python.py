word = "SECRET"
guess = ""
turns = 10

while turns>0:
    dashes = 0
    for i in word:
        if i in guess:
            print(i)
        else:
            print("_")
            dashes+=1
    if dashes == 0:
        print("You won")
        break
    print("")
    uguess = input("guess a character:-")
    if uguess not in word:
        print("Current guess is wrong")
    else:
        print("Current guess is correct")
    turns-=1
    print("remaining turns are",turns)
    guess+=uguess
    print("guess = ",guess)
    if turns==0:
        print("YOOU LOSE")
        
