def addFunction(istenilen,giris):
    import random
    numberlist = []
    for i in range(0,istenilen):
        number = random.randint(0,istenilen-1)

        inornot = number in numberlist
        if inornot == False:
            numberlist.append(number)

    inornot2 = giris in numberlist
    if inornot2 == True:
        print("Girdiğiniz sayı içeride")
    else:
        print("Girdiğiniz sayı içeride DEĞİL")
    print(numberlist)

def Input():
    while True:
        try:
            istenilen = int(input("Kaç sayılık bir küme istersiniz: "))
        except:
            print("Your input is false, try new input")
            continue
        else:
            break
            
    probability = 1-((istenilen-1)**istenilen)/(istenilen**istenilen)
    print(f"Now you wining probability is {probability}")
    
    while True:      
        try:
            giris = int(input(f"Hangi sayıyı bulmak istersiniz (Lütfen {istenilen}'den küçük bir sayı giriniz): "))
        except ValueError:
            print("Your input is false, please try a number with integers.")   
        else:    
            break
    
    addFunction(istenilen,giris)
Input()
