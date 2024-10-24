
def calculator():
    print("Input problem")
    input1 = int(input())
    operator = input()
    input2 = int(input())

    if operator == "+":
        result = input1 + input2
        print(f"= {result}")
    elif operator == "-":
        result = input1 - input2
        print(f"= {result}")
    elif operator == "*":
        result = input1 * input2
        print(f"= {result}")
    elif operator == "/":
        result = input1 / input2
        print(f"= {result}")
    else:
        print("invalid input, try again")
        calculator()
calculator()



