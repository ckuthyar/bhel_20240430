def genrand(n,qty):
    import random as rd
    list1=[]
    for i in range(0,qty,1):
        info1=rd.randint(10**(n-1),(10**n)-1)
        list1.append(info1)
    print(list1)

genrand(2,20)
genrand(4,10)
genrand(6,5)
