#Have the program find prime numbers until the user chooses to stop asking for the next one.

num = 1
prime_numbers = []

for i in range(1000):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

        num += 1

print("\n\nPress Enter for another number (Up to 1000)\nType 'END' to stop")

for i in range(100):
    choice = input()
    if choice == "END":
        exit()
    else:
        print(prime_numbers[i])