# Python Program to swap first and last element of the list.

# Examples:
# Input : [12, 35, 9, 76, 25]
# Output : [25, 35, 9, 76, 12]
# Input : [1, 2, 3]
# OutPut: [3, 2, 1]

# Approach 2:
# The Last element of the list can be reffered as list[-1]. Therefore we can simply swap list[0] with list[-1].
# Swap function
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList

# Driver Code
newList = [12, 35, 9, 76, 25]
print(swapList(newList)) 
# Time Complexity: O(1)
# Auxiliary Space: O(n), where n is length of list
