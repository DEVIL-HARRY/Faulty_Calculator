# Faulty Calculator
# 3 Wrong Ans
# Some Default Ans (45*3=555, 56+9=77, 56/6=4)

print("What you want to do\n Operators --> +, -, *, /")
n = input()

if n == "+":
    print("Enter number for Addition")
    print("Enter First num")
    n1 = int(input())
    print("Enter Second num")
    n2 = int(input())
    if n1 == 56 and n2 == 9:
        print(77)
    else:
        print(n1 + n2)

elif n == "-":
    print("Enter number for Subtraction")
    print("Enter First num")
    n1 = int(input())
    print("Enter Second num")
    n2 = int(input())
    print(n1 - n2)

elif n == "/":
    print("Enter number for Division")
    print("Enter First num")
    n1 = int(input())
    print("Enter Second num")
    n2 = int(input())
    if n1 == 56 and n2 == 6:
        print(4)
    else:
        print(n1 / n2)

elif n == "*":
    print("Enter number for Multiply")
    print("Enter First num")
    n1 = int(input())
    print("Enter Second num")
    n2 = int(input())
    if n1 == 45 and n2 == 3:
        print(555)
    else:
        print(n1 * n2)

else:
    print("Wrong Input")
