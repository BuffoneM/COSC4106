###
# Michael Buffone
# March 12th, 2021
# COSC4106 Assignment 3 : Question 1
#
# Write a program to implement the Horspool’s algorithm. Your program should ask the user to enter
# a text and a pattern, then output the following: 
# (a) shift table   
# (b) the searching result (whether the pattern is in the text or not)
###

def main():
    print("-----")
    userText = input("Enter a text: ")
    userPattern = input("Enter a pattern: ")
    print("\nGenerating the table for:", userPattern)
    
    shiftTable = generateShiftTable(userPattern)
    print(shiftTable)
        
    print("\nDoes '", userPattern, "' exist in '", userText, "'?\n-", sep="")
    if horspool(userText, userPattern, shiftTable):
        print(userPattern, " exists in the string '", userText, "'", sep = "")
    else:
        print(userPattern, " does not exist in the string '", userText, "'", sep = "")
    
    print("-----")

def generateShiftTable(pattern):
    shiftTable = []
            
    # For all of the characters in the string
    for i in range(0, len(pattern)):
        # If the array without char[i] still has the char[i] somewhere in it, continue
        if pattern[i+1 : len(pattern)].find(pattern[i]) != -1: 
            continue
        
        # Calculate the length from the end of the string, and append it with the current char 
        length = (len(pattern) - i - 1) if (i != len(pattern) - 1) else len(pattern)
        shiftTable.append([pattern[i], length])
        
    shiftTable.append(["", len(pattern)])      
    return shiftTable

def horspool(text, pattern, shiftTable):
    foundSubstring = False
    m = len(pattern) - 1
    index = 0
    
    while foundSubstring == False:
        if m >= len(text): return False        
        currentChar = text[m]
        index = m    
        tableLookup = findValue(shiftTable, currentChar)
        print(text[:m], "'", text[m], "'", text[m + 1:], sep="")
        
        # Lookup char[m], if it's the last table item compare the string
        if shiftTable[len(shiftTable) - 2] == tableLookup:
            foundString = True
            temp = 0
            print("Checking the string from the last lookup char...")
            
            # Loop through the substring found from the last char
            for i in range(index - len(pattern) + 1, index + 1):
                print("Pattern:", pattern[temp], "--- Table:", text[i])
                if pattern[temp] != text[i]:
                    # Add the null value and continue because we haven't found it
                    m += shiftTable[len(shiftTable) - 1][1]
                    foundString = False
                temp += 1
            
            if foundString == True:
                return True   
            
        # If we aren't at the last item in the table, add to m and continue            
        else:
            m += tableLookup[1]     
    
    return False

def findValue(array, key):
    for values in array:
        if key == values[0]: 
            return values
    
    return (array[len(array) - 1])
    
if __name__ == "__main__":
    main()