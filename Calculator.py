import time
print("Calculator Initiating")

Number1 = input("Please enter your first number:")
Number2 = input("Please enter your second number:")
Question = input("Which operation (add,multiply,divide) do you want to perform? :")

add = "add"
if Question == addition:
    print("You have opted to add")
    time.sleep(1)
    print("Please wait")
    time.sleep(2)
    print(int(Number1)+int(Number2))

multiply = "multiply"
if Question == multiply:
    print("You have opted to multiply")
    time.sleep(1)
    print("Please wait")
    time.sleep(2)
    print(int(Number1) * int(Number2))

if Question == "divide":
    print("You have opted to divide")
    time.sleep(1)
    print("Please wait")
    time.sleep(2)
    print(int(Number1) / int(Number2))
