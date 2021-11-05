import os

def print_menu():
    print(' -' + '-'*(46) + '-')
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Aditi                                |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(' -' + '-'*(46) + '-')
    print("")
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. stringLoop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")

def hello_world():
    print("Hello World")

def goodbye_world():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbye_person():
    print("Hello")
    name = input("What is your name ? ")
    print("Goodbye", name)

def goodbye_teacher():
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(name, "is an ok teacher")

def for_loop():
    for x in range(1, 500):
        print(x) 

def whileLoop():
    while True:
        name = input("What is the name of this subject ")
        if name == "IST":
            print("")
            print("")
            print(" Congratulations!!")
            print("")
            print("")
            break
        else:
            print("Not Correct - try again")

def stringLoop():
    string_name = input("What is your string? ")
    for element in range(0, len(string_name)):
        print(string_name[element])

def ascii():
    hello = input("What is your string? ")
    for element in hello:
        print(element, '=', ord(element))
while True:
    print_menu()
    menu = input("Enter an option ")
    print("")
    valid_options = ('1', '2', '3', '4', '5', '6', '7', '8', 'x')
    print("----Start of Output ---------------------------")
    print("")
    if menu in valid_options:
        if menu.lower() == 'x':
            print("\n----End of Output -----------------------------\n\n")
            print("Press Enter to continue ")
            break
        elif menu == '1':
            hello_world()
        elif menu == '2':
            goodbye_world()
        elif menu == '3':
            goodbye_person()
        elif menu == '4':
            goodbye_teacher()
        elif menu == '5':
            for_loop() 
        elif menu == '6':
            whileLoop()
        elif menu == '7':
            stringLoop()
        elif menu == '8':
            ascii()
    else:
        print("Invalid option")

    print("\n----End of Output -----------------------------\n\n")
    print("")

    input("Press Enter to continue ")



    





