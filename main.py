def show_result(value):
    print(value)
    if value == 15:
        print("That how old Chris is")


# this function adds two numbers,
def add(x,y):
    show_result(x + y)


# this function substracts two numbers,
def sub(x,y):
    show_result(x - y)


# this function multiplies two numbers,
def mul(x,y):
    show_result(x*y)


# this function divides two numbers,
def div(x,y):
    show_result(x/y)


def check_age_message(value):
    if value == 15:
        print("That how old Chris is")


######################## start of program ########################

def main():
    print("Welcome to the calculator app.")
    print("What would you like to do?")
    while(True):
        print("Type (a)dd, (s)ubtract, (m)ultiply, (d)ivide, or (q)uit")
        user_choice=input(": ")
    ##print(user_choice)
        if user_choice == 'a':
            x = int(input("Enter the first number: "))
            y = int(input("Enter the first number: "))
            check_age_message(x)
            check_age_message(y)
            add(x,y)
        elif user_choice == 's':
            x = int(input("Enter the first number: "))
            y =int(input("Enter the first number: "))
            check_age_message(x)
            check_age_message(y)
            sub(x,y)
        elif user_choice == 'm':
            x = int(input("Enter the first number: "))
            y = int(input("Enter the first number: "))
            check_age_message(x)
            check_age_message(y)
            mul(x,y)
        elif user_choice == 'd':
            x = int(input("Enter the first number: "))
            y = int(input("Enter the first number: "))
            check_age_message(x)
            check_age_message(y)
            div(x,y)
        elif user_choice == 'q':
            print("Shutting...downq")
            break
        else:
            print("Wrong thing, try again.")


if __name__ == "__main__":
    main()