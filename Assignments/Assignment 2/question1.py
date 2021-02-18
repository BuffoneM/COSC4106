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

def mergeSort(array, left, right):
    count = 0
    if left < right:
        # Split the problem into two, then add the count result for each half
        middle = (left + right) // 2
        count += mergeSort(array, left, middle)
        count += mergeSort(array, middle + 1, right)
        count += merge(array, left, middle, right)
    return count
    
def merge(array, left, middle, right):
    leftArray = array[left:middle + 1]
    rightArray = array[middle + 1: right + 1]
    print(leftArray, rightArray)
    
    i = 0
    j = 0
    k = left
    count = 0

    # Increment count when the value in the left array is > value in right array
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            count += (middle + 1) - (left + i)
            j += 1
        k += 1        
    
    while i < len(leftArray):
        array[k] = leftArray[i]
        i += 1
        k += 1
    while j < len(rightArray):
        array[k] = rightArray[j]
        j += 1
        k += 1
    
    return count

def main():
    print("-----")
    array = [9, 8, 4, 5]
    print("Splitting ", array, " into pieces:", sep="")
    print("The number of inversions with the array", array, "is:", mergeSort(array, 0, len(array) - 1))
    print("-----")


if __name__ == "__main__":
    main()
