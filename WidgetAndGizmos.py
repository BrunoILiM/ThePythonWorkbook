#
##Compute the total weight of your gizmos and widgets
#

#Initialize the GIZMO_WEIGHT and the WIDGET_WEIGHT with its weight
GIZMO_WEIGHT=112
WIDGET_WEIGHT=75

#Read the input values from the user
widgets=int(input("How many widgets do you have?: "))
gizmos=int(input("How many gizmos do you have?: "))

#Calculate the weight
totalWeight=(widgets*WIDGET_WEIGHT)+(gizmos*GIZMO_WEIGHT)

#Display the result
print("Your total weight is :", totalWeight)
