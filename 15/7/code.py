for a in range(128):
    b = 1
    for x in range(128):
        if not(((x&77)==0) or ((x&12)!=0) or ((x&a)!=0)):
            b = 0
    if b == 1:
        print(a)