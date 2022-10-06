for a in range(32):
    b = 1
    for x in range(32):
        if not(((x&29)==0) or ((x&12)!=0) or ((x&a)!=0)):
            b = 0
    if b==1:
        print(a)