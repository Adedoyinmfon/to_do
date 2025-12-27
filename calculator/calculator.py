def calculate(num1, num2, operations):
  #for operation in operations:
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
      
  elif operation == "/":
    if num2 == 0:
      return "Error: Cannot divide by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operation"
    
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+ - * /): ")

    result = calculate(num1, num2, operation)
    print("Result:", result)

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again == "no":
        print("Calculator stopped.")
        break
