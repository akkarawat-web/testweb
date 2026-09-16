try:
    value=int(input("Enter a number:"))
    result = 10/value
except ZeroDivisionError:
    print("cannot divide by Zero!")
else:
    print(f"the result is {result}")
print("End of progarm")