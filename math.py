try:
  a=float(input("Enter your first number:"))
  b=float(input("Enter your second number:"))
  print(f"addition:{a+b}")
  print(f"subtraction:{a-b}")
except ValueError:
  print("Please enter valid numbers.")
