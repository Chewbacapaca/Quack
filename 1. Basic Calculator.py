print("BASIC CALCULATOR: Do your basic math.")
a = float(input("First Number: "))
o = input("Operator (+, -, *, /): ")
b = float(input("Second Number: "))
if o == "+":
    c = a + b
    print("Answer: ", c)
elif o == "-":
    c = a - b
    print("Answer: ", c)
elif o == "*":
    c = a * b
    print("Answer: ", c)
elif o == "/":
    c = a/b
    print("Answer: ", c)
elif o != ("+" or "-" or "*" or "/"):
    print("Invalid operator")
