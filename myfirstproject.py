def main():
    name = input("What is your name?")
    print("Hello ", name)

    x = 10
    print(x)

    number = int(input("Enter in a number: "))
    if number > 10:
        print(number, "is greater than 10")
    elif number == 10:
        print("that number is 10")
    else:
        print(number, "is less than 10")
    number = int(input("Enter in a number: "))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, " is odd")

    my_list = ["Adam","Dylan","Kira","Lake","Mizuki","Nathaniel","Roman","Sheridan","Wyatt"]
    for name in my_list:
        print(name)

if __name__ == "__main__":
    main()


