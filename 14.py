def genOTP(n):
    import random as rd
    for i in range(0,10,1):
        info2=rd.randint(10**(n-1),(10**n)-1)
        print(info2)
genOTP(4)
genOTP(6)
