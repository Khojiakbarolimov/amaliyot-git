name = input("Filename = ").split(".")
symbol = input("Symbol = ").split(".")
check = True
if len(symbol) == 1 and symbol[0] =="*":
    print(check)
elif symbol[0] == "*":
    if name[1] == symbol[1]:
        print(check)
    else:
        print(False)
else:    
    if name[1] == symbol[1] and len(name[0]) == len(symbol[0]):   
        for i, val in enumerate(name[0]):
            if val != symbol[0][i] and symbol[0][i] != "?":
                check = False
                break
        print(check)
    else:
        print(False)