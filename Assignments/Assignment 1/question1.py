###
# Michael Buffone
# February 2nd, 2021
# COSC4106 Assignment 1 : Question 1
#
# Given a string of characters, count the number of substrings that start with an A and end with a B. 
# For example, there are four such substrings in CABAAXBYA, i.e. AB, ABAAXB, AAXB, AXB. 
# Write a program that uses the brute-force approach to count the number of such substrings in a 
# given string.
###

# Start of countAB function #
def countAB(userString):

    count = 0

    # Let i be the A we are looking for
    # Let j be the B we are looking for
    for i in range(0, len(userString)):
        if userString[i] == "A":
            for j in range(i, len(userString)):
                if userString[j] == "B":
                    print("Substring found:", userString[i:j+1])
                    count += 1
    return count
# End countAB #

def main():
    print("-----")
    userString = input("Please enter a string: ")
    print("The number of substrings that start with an A and end with a B is", countAB(userString))
    print("-----")
    
if __name__ == "__main__":
    main()