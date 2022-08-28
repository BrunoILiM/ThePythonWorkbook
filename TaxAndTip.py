TIP=.18
TAX=.16
cost=float(input("Enter the cost of the meal "))

onlyTip=cost+(cost*TIP)
onlyTax=cost+(cost*TAX)
grandTotal=cost+(cost*TIP)+(cost*TAX)

print(onlyTip,onlyTax,grandTotal)