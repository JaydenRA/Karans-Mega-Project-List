#The user enters a cost and then the amount of money given. 
#The program will figure out the change and the number of which notes/coins needed for the change.

cost = float(input("Price (£): "))
moneyGiven = float(input("Money Given (£): "))
change = moneyGiven - cost

totalChange = []

while change > 0.01:
    while change >= 50:
        change = change - 50
        totalChange.append("£50")

    while change >= 20:
        change = change - 20
        totalChange.append("£20")

    while change >= 10:
        change = change - 10
        totalChange.append("£10")

    while change >= 5:
        change = change - 5
        totalChange.append("£5")

    while change >= 1:
        change = change - 1
        totalChange.append("£1")

    while change >= 0.5:
        change = change - 0.5
        totalChange.append("50p")

    while change >= 0.2:
        change = change - 0.2
        totalChange.append("20p")

    while change >= 0.1:
        change = change - 0.1
        totalChange.append("10p")
    
    while change >= 0.05:
        change = change - 0.05
        totalChange.append("5p")

    while change >= 0.02:
        change = change - 0.02
        totalChange.append("2p")

    while change >= 0.01:
        change = change - 0.01
        totalChange.append("1p")

print(f"Change = {totalChange}")
    