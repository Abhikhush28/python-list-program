# Python Program to swap first and last element of the list.

# Examples:
# Input : [12, 35, 9, 76, 25]
# Output : [25, 35, 9, 76, 12]
# Input : [1, 2, 3]
# OutPut: [3, 2, 1]

# Approach 1:
# Find the length of the list and simply swap the first element with (n-1)th element.

# Swap function
def swapList(newList):
    size = len(newList)
    
    # Swapping
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    return newList

# Driver Code
newList = [12, 35, 9, 76, 25]
print(swapList(newList)) 