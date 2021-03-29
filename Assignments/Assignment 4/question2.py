###
# Michael Buffone
# March 29th, 2021
# COSC4106 Assignment 4 : Question 2
#
###
def recursiveSolution(workSchedule, n):
    if(n == 0):
        return max(workSchedule[0][n], workSchedule[1][n])
    
    if(recursiveSolution)
    
    return max(workSchedule[0][n-1], workSchedule[1][n-1]) + recursiveSolution(workSchedule, n-1)

def main():
    print("-----")
    
    n = 4
    workSchedule = [[10, 1, 10, 10], 
                    [5, 50, 5, 1]]
    
    print("The value of the current work schedule is:", recursiveSolution(workSchedule, n))
    
    print("-----")
    
if __name__ == "__main__":
    main()