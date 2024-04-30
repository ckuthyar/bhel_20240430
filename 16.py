def genOTP(n,qty):
    import random as rd
    list1=[]
    for i in range(0,qty,1):
        otp=rd.randint(10**(n-1),(10**n)-1)
        list1.append(otp)
    return list1
print(genOTP(4,10))
print(genOTP(6,5))


