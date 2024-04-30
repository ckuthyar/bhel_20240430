import mod_otp as mo
banks=["ICICI","HDFC","HSBC","SBI"]
size=[4,6,8,6]
qty=[20,10,5,40]

bank1=banks[0]
size1=size[0]
qty1=qty[0]

result=mo.genOTP(size1,qty1)
print(bank1,":",result)

