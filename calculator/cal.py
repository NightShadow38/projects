equ = input("Equation: ")
array = ['']

for ele in equ:
    if ele in "1234567890":
        array[-1] += ele
    elif ele in "+-/*^":
        array.append(ele)
        array.append("")


total = 0
operator = "+"

for ele in array:
    if ele in "+-/*^":
        operator = ele
    else:
        if operator == "+":
            total = total + int(ele)
        elif operator == "-":
            total = total - int(ele)
        elif operator == "*":
            total = total * int(ele)
        elif operator == "/":
            total = total / int(ele)
        elif operator == "^":
            total = total ** int(ele)
        else:
            print("ERROR")

print(total)
