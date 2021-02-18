###
# Michael Buffone
# February 18th, 2021
# COSC4106 Assignment 2 : Question 2
#
# Given two lists of n integers A, B and a sum S, where all the elements in each 
# list are unique, write a program that uses a transform-and-conquer algorithm with 
# efficiency class O(nlogn) to decide whether there is an integer from A and an 
# integer from B such that the sum of these two integers is equal to S.
#
# For example, if A = {8, 3, 4, 7} and B = {5, 6, 12, 1} and S is 10, then your 
# program should output “4 + 6 = 10” (where 4 is from A and 6 is from B).
# 
# Another example, if A = {1, 5, 4, 2} and B = {6, 3, 2, 1} and S is 9, 
# then your program should output “No two integers from A and B add up to 9”.
###


# O(nlogn) sorting algorithm from question 1
def mergeSort(array, left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    mergeSort(array, left, middle)
    mergeSort(array, middle + 1, right)
    merge(array, left, middle, right)
    
def merge(array, left, middle, right):
    leftArray = array[left:middle + 1]
    rightArray = array[middle + 1: right + 1]
    
    i = 0
    j = 0
    k = left
    
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
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

def binarySearch(array, item):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        middle = (low + high) // 2
        if array[middle] == item:
            return middle
        elif array[middle] < item:
            low = middle + 1
        else:
            high = middle - 1
    
    return -1                

def solve(arrayA, arrayB, sum):
    # Sort the arrays
    print("Sorting the arrays with merge sort:", arrayA, "and", arrayB)
    mergeSort(arrayA, 0, len(arrayA) - 1)
    mergeSort(arrayB, 0, len(arrayB) - 1)
    print(arrayA, "and", arrayB)
    
    answer = []
    for currentVal in arrayA:
        # Key = 2nd number we need to add to 1st number to get sum
        key = sum - currentVal
        index = binarySearch(arrayB, key)
        
        # If the key is found in the 2nd array, set answer and break out
        if index != -1:
            answer = [currentVal, arrayB[index]]
            break
    
    if answer != []:
        print(answer[0], "+", answer[1], "=", sum)
    else:
        print("No two integers from A and B add up to", sum)

def main():
    print("-----")
    arrayA = [8, 3, 4, 7]
    arrayB = [5, 6, 12, 1]
    sum = 10
    solve(arrayA, arrayB, sum)
    print()
    
    arrayA = [1, 5, 4, 2]
    arrayB = [6, 3, 2, 1]
    sum = 9
    solve(arrayA, arrayB, sum)
    print("-----")

if __name__ == "__main__":
    main()