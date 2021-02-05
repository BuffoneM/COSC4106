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

def findPowerSet(userList):
    powerSet = [[]]
    # for every element in userList
    for item in userList:
        # for every subset in the powerset
        for subSet in powerSet:
        # add the subset plus the current item to the powerset
            powerSet = powerSet + [(subSet + [item])]
    print(powerSet)

    # sum all of the items in the power set
    newArray = []
    for item in powerSet:
         newArray.append(sum(item))

    return newArray
    
def main():
    print("-----")
    # data declaration
    value = -1
    capacity = 9
    tempArrayWeight = [8, 4, 5]
    tempArrayValue = [20, 10, 11]

    print("Calculating the power sets:")
    tempArrayWeight = findPowerSet(tempArrayWeight)
    tempArrayValue = findPowerSet(tempArrayValue)
    print()
    print(tempArrayWeight)
    print(tempArrayValue)
    print()

    # get the best value for the weight
    for i in range(0, len(tempArrayWeight)):
        if tempArrayWeight[i] <= capacity and value < tempArrayValue[i]:
            value = tempArrayValue[i]

    print("The capacity of the knapsack is", capacity)
    print("The largest value that fits into the knapsack:", value)
    print("-----")

if __name__ == "__main__":
    main()