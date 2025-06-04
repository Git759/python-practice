number1 = input("Enter the number :")
num1 = int(number1)
if num1%4==0 and num1%3==0:
 print((num1), "is divisible by 4 and 3")
elif num1%4==0:
 print ((num1),"is divisible by 4")
elif num1%3==0:
 print((num1),"is divisible by 3")
else:
 print((num1), "is not divisible by 3 and 4")

 