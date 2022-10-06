for a in range(64):
    b = True
    for x in range(64):
        if not((x&41==0) or (x&33!=0) or (x&a!=0)):
            b = False
    if b == True:
        print(a)
