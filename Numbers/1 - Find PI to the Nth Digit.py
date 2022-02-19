#Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

from mpmath import mp

mp.dps = int(input("Decimal Points: ")) + 1 
print(mp.pi)