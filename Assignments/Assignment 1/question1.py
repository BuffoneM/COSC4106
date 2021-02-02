###
# Michael Buffone
# February 2nd, 2021
# COSC4106 Assignment 1
#
# Given a string of characters, count the number of substrings that start with an A and end with a B. 
# For example, there are four such substrings in CABAAXBYA, i.e. AB, ABAAXB, AAXB, AXB. 
# Write a program that uses the brute-force approach to count the number of such substrings in a 
# given string.
###

# Start of countAB function #
def countAB(userString):

    # Pre condition that the string is only 2 letters long
    if userString == "AB":
        print("Substring found:", userString)
        count = 1
    else:
        count = 0

    # Let i be the A we are looking for, go to the second last letter
    # Let j be the B we are looking for
    for i in range(0, len(userString)-2):
        for j in range(i+1, len(userString)):
            if userString[i] == "A" and userString[j] == "B":
                print("Substring found:", userString[i:j+1])
                count+=1
    return count
# End countAB #

print("-----")
userString = input("Please enter a string: ")
print("The number of substrings that start with an A and end with a B is", countAB(userString))
print("-----")