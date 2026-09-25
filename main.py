# this function adds two numbers,
def add(x,y):
    print(x + y)


# this function substracts two numbers,
def sub(x,y):
    print(x - y)


# this function multiplies two numbers,
def mul(x,y):
    print(x*y)


# this function divides two numbers,
def div(x,y):
    print(x/y)


######################## start of program ########################

print("Welcome to the calculator app.")
print("What would you like to do?")
while(True):
    print("Type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, or (q)uit")
    user_choice=input(": ")
##print(user_choice)
    if user_choice == 'a':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the first number: "))
        add(x,y)
    elif user_choice == 's':
        x = int(input("Enter the first number: "))
        y =int(input("Enter the first number: "))
        sub(x,y)
    elif user_choice == 'm':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the first number: "))
        mul(x,y)
    elif user_choice == 'd':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the first number: "))
        div(x,y)
    elif user_choice == 'q':
        print("Shutting...downq")
        break
    else:
        print("Wrong thing, try again.")