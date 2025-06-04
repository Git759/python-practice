number1 = input("Enter the number :")
num1 = int(number1)
i=1
if num1>20:
    print ("outside the loop")
else:
    while i <= num1:
        print(i)
        i=i+1
        print("inside while loop")
