##
#Compute the refund for the drink container
#

LESS_DEPOSIT=.10
MORE_DEPOSIT=.25

#Read the input values from ther user
less=int(input("How many containers of 1 litre or less do you have? "))
more=int(input("How many containers more that 1 litre do you have? "))

#Calculate the refund amount
refund=(less*LESS_DEPOSIT)+(more*MORE_DEPOSIT)

#Print the result
print("Your total refund will be $%.2f"%refund)