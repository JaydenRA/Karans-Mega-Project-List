#Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

from mpmath import mp

mp.dps = int(input("Decimal Points: ")) + 1 
print(mp.e)