number1 = input("Enter the first number ")
number2 = input("Enter the second number ")
number3 = input("Enter the third number ")
num1 = int(number1)
num2 = int(number2)
num3 = int(number3)
if num1>=num2 and num1>=num3:
 print(str(num1)+ " is the greatest")
elif num2>=num3 and num2>=num1:
 print(str(num2)+ " is the greatest")
else:
 print(str(num3)+ " is the greatest")
