#Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
#Also figure out how long it will take the user to pay back the loan. 
#For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

months = int(input("Length of Contract (months): "))
loan = int(input("Loan Taken (£): "))
interest = int(input("Interest Rate (%): "))

print(f"Amount due per month: {(loan * (1+interest/100))/months}")