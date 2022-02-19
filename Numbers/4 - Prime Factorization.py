#Have the user enter a number and find all Prime Factors (if there are any) and display them.

from math import sqrt

n = int(input("Number: "))
PrimeFactors = []

while n % 2 == 0:
    PrimeFactors.append(2)
    n = n/2

for i in range(3, int(sqrt(n))+1 ,2):
    while n % i == 0:
        PrimeFactors.append(i)
        n = n/i

if n > 2:
    PrimeFactors.append(n)

if len(PrimeFactors) > 0:
    print(PrimeFactors)
else:
    print("No Prime Factors")