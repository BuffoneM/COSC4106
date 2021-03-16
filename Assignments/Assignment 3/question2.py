###
# Michael Buffone
# March 15th, 2021
# COSC4106 Assignment 3 : Question 2
#
# A contractor is given a list of n jobs. Each job takes exactly one hour to finish. 
# Each job ji has a profit pi (pi  > 0) and a deadline di (1 <= di <= n).  The 
# profit is earned only if the job is completed by the deadline. Design and implement 
# a greedy algorithm to create a job schedule that maximizes the profit.  A job 
# schedule is a list of the selected jobs in the order they should be completed. A 
# job should not be selected if the contractor cannot complete it before the deadline.
###

class Job:
    id = ''
    profit = ''
    deadline = ''
    
    def __init__(self, id, profit, deadline):
        self.id = id
        self.profit = profit
        self.deadline = deadline
    
    def getID(self):
        return self.id
    
    def getProfit(self):
        return self.profit
    
    def getDeadline(self):
        return self.deadline
    
    def toString(self):
        return self.id, self.profit, self.deadline

def greedyTechnique(array):
    # Sort the array based on profit, and get the longest deadline
    array.sort(key = lambda item: item.profit)
    numJobs = max(array, key = lambda item: item.deadline).getDeadline()
    print("The sorted list of jobs is:")
    for job in array: print(job.toString())
    print("The maximum number job deadline is:", numJobs)

    bestJobs = []
    profit = 0
    numJobs += 1
    for i in range (numJobs):
        print(numJobs)
        curr = array.pop()
        
        numJobs -= 1
        if curr.getDeadline() <= numJobs:
            bestJobs.append(curr)
            profit += curr.getProfit()
        else:
            numJobs += 1
        
        
    print("\nThe jobs that should be completed are:")
    for job in bestJobs: print(job.toString())
    print("Max profit =", profit)
    print("---")    
    
def main():
    print("-----")
    
    jobExample1 = [
            Job("j1", 100, 2),
            Job("j2", 10, 1),
            Job("j3", 15, 2),
            Job("j4", 27, 1)
        ]
    jobExample2 = [
            Job("j1", 5, 3),
            Job("j2", 15, 2),
            Job("j3", 10, 1),
            Job("j4", 20, 2),
            Job("j5", 1, 3)
        ]
    
    greedyTechnique(jobExample1)
    greedyTechnique(jobExample2)
    
    print("-----")
    
if __name__ == "__main__":
    main()