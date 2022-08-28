##
#Compute the area of a field, reporting in acres
#

#We start the SquareFeetPerAcre constant with the value of how many feet there are in a acre
SQUARE_FEET_PER_ACRE=43,560

#Read the input values from the user
length=float(input("Enter the length of the room in feet: "))
width=float(input("Enter the width of the room in feet: "))

#Calculate the acres
acres=(length*width)/SQUARE_FEET_PER_ACRE

#Print the result
print("The acres in your field are: ",acres,"acres")
