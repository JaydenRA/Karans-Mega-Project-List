# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def main():
    while True:
        choice = int(input("\n1 - Binary to Denary\n2 - Denary to Binary\n9 - Exit\n\nChoice: "))
        if choice == 1:
            b2d()
        elif choice == 2:
            d2b()
        elif choice == 9:
            exit()

def b2d():
    num = input("Binary Number (eg 0011): ")
    print(f"Binary: {num}\nDenary: {int(num, 2)}")

def d2b():
    num = int(input("Binary Number (eg 21): "))
    binaryNum = bin(num)
    print(f"Denary: {num}\nBinary: {binaryNum[2:]}")

main()