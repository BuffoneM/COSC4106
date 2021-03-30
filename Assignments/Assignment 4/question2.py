###
# Michael Buffone
# March 29th, 2021
# COSC4106 Assignment 4 : Question 2
#
###
def solve(workSchedule, n):
    # Base case 1: the "none" case
    if(n == 0):
        return 0
    
    # Base case 2: return the better job if for low / high stress
    if(n == 1):
        return max(workSchedule[0][n-1], workSchedule[1][n-1])
    
    return max(workSchedule[0][n-1] + solve(workSchedule, n-1), workSchedule[1][n-1] + solve(workSchedule, n-2))

def main():
    print("-----")
    
    n = 4
    workSchedule = [[10, 1, 10, 10], 
                    [5, 50, 5, 1]]
    
    print("The best value of the work schedule is:", solve(workSchedule, n))
    
    print("-----")
    
if __name__ == "__main__":
    main()