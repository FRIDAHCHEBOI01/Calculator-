#hi loveee:)
'''
how was your night!)
'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("Please select operation to be made")
print('''Add 1
Subtract 2
Divide 3
Multiply 4''')
choice  = input("Enter choice of operation(must be a number)")
if choice in ['1','2','3','4']:
    num1 = int(input("Please enter first integer:"))
    num2 = int(input("Please enter second integer:"))
    #blah blah code goes in here
    if choice == '1':
        print("The answer is {}".format(add(num1,num2)))
    if choice == '2':
        print("The answer is {}".format(subtract(num1,num2)))
    if choice == '3':
        print("The answer is {}".format(divide(num1,num2)))
    if choice == '4':
        print("The answer is {} ".format(multiply(num1,num2)))
else:
    print("Invalid choice!")
