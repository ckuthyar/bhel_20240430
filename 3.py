def genrand(n,qty):
    import random as rd
    list1=[]
    for i in range(0,qty,1):
        info1=rd.randint(10**(n-1),(10**n)-1)
        list1.append(info1)
    print(list1)

banks=['ICICI','HDFC','HSBC','SBI']
len1=len(banks)

size=[4,6,8,6]
rates=[1,1,1,1]
qty=[1000,500,200,9000]
bill=[]


for i in range(0,len1,1):
    genrand(size[i],qty[i])
    bill.append(qty[i]*rate[i])
    print("Bill for ", banks[i],"is",bill[i])
print(bill)
print("Total revenue for Infosys is", sum(bill))








