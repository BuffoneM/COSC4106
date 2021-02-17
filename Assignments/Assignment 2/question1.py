###
# Michael Buffone
# February 14th, 2021
# COSC4106 Assignment 2 : Question 1
#
# Let a[0..n-1] be an array of n distinct integers. A pair (a[i], a[j]) is said to 
# be an inversion if these numbers are out of order, i.e., i < j but a[i] > a[j].
#
# For example: if array a contains the following numbers: 9, 8, 4, 5
# then the number of inversions is 5. 
# (inversions are 9 > 8,  9 > 4,  9 > 5,  8 > 4,  8 > 5)
###

def countInversions(array):
    if len(array) <= 1:
        return
    if(len(array) == 2):
        if array[0] > array[1]:
            print("Inversion pair:", array[0], ">", array[1])
            return 1
        else:
            print("Inversion pair:", array[0], "!>", array[1])
            return 0
    
    halfPoint = len(array) // 2
    leftArray = array[:halfPoint]
    rightArray = array[halfPoint:]
    
    return countInversions(leftArray) + countInversions(rightArray)

def countInversions2(array, index):
    # -if the array is empty, return 0
    # -if we've compared all items, remove the first element in the
    #  array and restart at index 1 (We don't compare the item to itself)
    if(array == []):
        return 0
    if(index == len(array)):
        print()
        return countInversions2(array[1:], 1)
    
    print(array, " at ", index, ": ", end="", sep="")    

    # recursive call- if inversion, add 1
    if(array[0] > array[index]):
        print(array[0], ">", array[index])
        return 1 + countInversions2(array, index + 1)
    else:
        print(array[0], "!>", array[index])
        return countInversions2(array, index + 1)
    
def main():
    print("-----")
    print("The inversion pairs are:")
    array = [9, 8, 4, 5]
    print("The number of inversions with the array", array, "is:", countInversions(array))

    print("-----")

if __name__ == "__main__":
    main()