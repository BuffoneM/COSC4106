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
                substringSolution += x[i]
                print(substringSolution)
                array[i][j] = array[i-1][j-1] + 1
            else:
                substringSolution = ""
                array[i][j] = max(array[i-1][j], array[i][j-1])
                              
    print2dArray(x, y, m, n, array)
    return substringSolution
     
def main():
    print("-----")
    
    x = "xABCB"
    y = "yBDCAB"
    m = len(x)
    n = len(y)
    array = [[0 for i in range(n)] for j in range(m)]
    
    print("X string:", x[1:])
    print("Y string:", y[1:])
    print("m =", m-1)
    print("n =", n-1)
    print()
    print2dArray(x, y, m, n, array)
    print("Solving longest common subsequence for Y and Y:")
    answer = subsequenceSolver(x, y, array, m, n)
    print("The longest subsequence is:", answer)
    print("-----")
    
if __name__ == "__main__":
    main()