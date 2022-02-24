# Write a pseudo-code description of a function that reverses a list of n integers, 
# so that the numbers are listed in the opposite order than they were before, 
# and compare this method to an equivalent Python function for doing the same thing.

def myReverse(arr):
    i = 0
    j = len(arr) - 1
    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

# Driver code to test
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5]
print("Original array:", arr1)
myReverse(arr1)
print("Reversed array using my own function:", arr1)
arr2.reverse()
print("Reversed array using Python's function:", arr2)