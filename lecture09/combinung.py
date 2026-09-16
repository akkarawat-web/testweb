try:
    value = int(input("enter a number:"))
    result = 10 / value
except ValueError:
    print("Invalid input ! please enter a nuber.")
except ZeroDivisionError:
    print("Cannot divide by zero !")
else:
    print(f"the result is {result}")
finally:
    print("Execution completed.")