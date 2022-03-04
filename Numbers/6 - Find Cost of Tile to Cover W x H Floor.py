#Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

price = int(input("Price of tile /m^2: £"))
w = int(input("Width (m): "))
l = int(input("Length (m): "))

print(f"£{price*w*l}")