###
# Michael Buffone
# February 2nd, 2021
# COSC4106 Assignment 1 : Question 2
#
# Write a program that uses the brute-force approach to solve the 0/1 knapsack problem. 
# Suppose there are n items with weights w1, w2, ..., wn and values v1, v2, ..., vn and 
# a knapsack of capacity W. Use the decrease-by-one technique to generate the power set 
# and calculate the total weights and values of each subset, then find the largest value 
# that fits into the knapsack and output that value. 
#
# For example: If there are 3 items with the following weights and values and the capacity 
# of the knapsack is 9, your program should then calculate the total 
# weight and the total value of each subset in the power set:
# -
# weight: 8 4 5
# value:  20 10 11
# total weight of subset: 0, 8, 4, 12, 5, 13, 9, 17
# total value of subset:  0, 20, 10, 30, 11, 31, 21, 41
# The largest value that fits into the knapsack: 21.
###

# Start of Item definition #
class Item:
    itemCount = 0

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        Item.itemCount += 1
    
    def showItem(self):
        print("Weight:", self.weight, "Value:", self.value)
# End Item definition #

# Start of main #
print("-----")
myList = [
            Item(8, 20),
            Item(4, 10),
            Item(5, 11)
         ]

for items in myList:
    items.showItem()
print("-----")
# End of main #