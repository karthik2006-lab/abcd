try:
  a=float(input("Enter your first number:"))
  b=float(input("Enter your second number:"))
  print(f"addition:{a+b}")
  print(f"subtraction:{a-b}")
  print(f"multiplication:{a*b}")
  if b!=0:
    print(f"Division :{a/b}")
  else:
    print("Division by zero is not allowed.")
except ValueError:
  print("Please enter valid numbers.")
