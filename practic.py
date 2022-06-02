while True:
    a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
    if (a2 > a1 < b2 and a2 > b1 < b2) or (a2 < a1 > b2 and a2 < b1 > b2):
        print('пустое множество')
    elif a1 > a2:#1
        if b1 == b2:
            print(a1, b1)
        elif b1 > b2:
            if a1 == b2:
                print(a1)
            else:    
                print(a1, b2)
        elif b1 < b2:
            print(a1, b1)        
    elif  a1 < a2:#2
        if b1 == b2:
            print(a2, b1)
        elif b1 > b2:
            print(a2, b2)
        elif b1 < b2:
            if b1 == a2:
                print(a2)
            else:
                print(a2, b1)
    elif a1 == a2:
        if b1 == b2:
            if a1 != b1:
                print(a1, b1)
            else:
                print(a1)
        elif b1 < b2:
            if b1 == a2:
                print(a2)
            else:
                print(a1, b1)
        elif b1 > b2:
            if b1 == a2:
                print(a2)
            else:
                print(a1, b1)
     
