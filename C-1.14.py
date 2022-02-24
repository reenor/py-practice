# Write a short Python function that takes a sequence of integer values and determines if
# there is a distinct pair of numbers in the sequence whose product is odd.

# Example:
# Input: arr[] = {1, 5, 2, 2}

# There are 3 distinct pairs, they are {1, 5}, {1, 2}, {5, 2}
# {2, 2} IS NOT a distinct pair
# {1, 5} is a distinct pair whose product is odd

def hasOddProduct(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if (arr[i] != arr[j]):
                if (arr[i] * arr[j]) & 0x01 == 1:
                    return True
    return False
            
# Driver code to test
arr1 = [2, 4, 6, 8] 
arr2 = [1, 6, 4, 7, 8]
print(arr1, "->", hasOddProduct(arr1)) # False
print(arr2, "->", hasOddProduct(arr2)) # True because of {1, 7}