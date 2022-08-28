#
##A simple code to calculate the cost of a meal with Tip, Tax and both
#

#Initialize the TIP and the TAX variable with its values
TIP=.18
TAX=.16

#Read the input value from the user
cost=float(input("Enter the cost of the meal "))

#Calculate the cost of the meal with only the tip, the tax and both
onlyTip=cost+(cost*TIP)
onlyTax=cost+(cost*TAX)
grandTotal=cost+(cost*TIP)+(cost*TAX)

#Display the result
print(onlyTip,onlyTax,grandTotal)
