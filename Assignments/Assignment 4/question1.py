###
# Michael Buffone
# March 27th, 2021
# COSC4106 Assignment 4 : Question 1
#
# Write a program to solve the Longest Common Subsequence problem using dynamic programming
# as discussed in class. For example if the input is:
# X = ABCBDAB
# Y = BDCABA
# Output = BCBA
###

def print2dArray(x, y, m, n, array):
    # Print the top values
    print("  ", end=" ")
    for i in range(0, n):
        print(y[i], end="  ")
    print()
    # Print the arrays
    for i in range(0, m):
        print(x[i], array[i])
        
def subsequenceSolver(x, y, array, m, n): 
    substringSolution = ""
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                array[i][j] = array[i-1][j-1] + 1
            else:
                array[i][j] = max(array[i-1][j], array[i][j-1])
    
    # Get the longest subsequence from the last row in the sequence array
    for i in range(1, n):
        # Only add the characters from y where it changes in the array
        if array[m-1][i] == array[m-1][i-1]: continue
        substringSolution += y[i]
                                  
    print2dArray(x, y, m, n, array)
    return substringSolution

def solver(x, y):
    x = "x" + x
    y = "y" + y
    m = len(x)
    n = len(y)
    array = [[0 for i in range(n)] for j in range(m)]
    
    print("X string:", x[1:], "\nY string:", y[1:])
    print("m =", m-1, "\nn =", n-1, "\n")
    print2dArray(x, y, m, n, array)
    print("\nSolving longest common subsequence for X and Y:")
    print("The longest subsequence is:", subsequenceSolver(x, y, array, m, n))
     
def main():
    print("-----")

    solver("ABCB", "BDCAB")
    print("---")
    solver("ABCBDAB", "BDCABA")
    
    print("-----")
    
if __name__ == "__main__":
    main()