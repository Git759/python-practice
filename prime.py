number=int(input("Enter the number "))
i=2
while i<number:
 if number%i==0:
  print("number is not prime")
  break
 else:
  print("number is prime")
 i=i+1