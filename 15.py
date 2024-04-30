def genOTP(n,qty):
    import random as rd
    for i in range(0,qty,1):
        info2=rd.randint(10**(n-1),(10**n)-1)
        print(info2)
genOTP(4,10) #generate 10 numbers of 4-digit OTP
print()
genOTP(6,5) #generate 5 numbers of 6-digit OTP
