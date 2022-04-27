from colourIdentification import ColourIden




def main():

    print("Image Processing System:\n\n")
    print("How Would you like to process your image?\n")
    print("Choose Below:\n")
    print("1. Image Enhancement")
    print("2. Colour Identification")
    print("3. Shape Identification")
    print("4. Object Identification")
    print("5. Object Manipulation")

    print("Type your choice here:\n\n ")
    choice = int(input())
    while choice > 6:
        print("Type your choice here:\n\n ")
        choice = int(input())
    print(choice)

    if choice == 1:
        print("Image Enhancement program")
    elif choice == 2:
        print("Colour Identification")
        ColourIden()
    elif choice == 3:
        print("Shape Identification")
    elif choice == 4:
        print("Object Identification")
    elif choice == 5:
        print("Object Manipulation")

    main()


    return

main()