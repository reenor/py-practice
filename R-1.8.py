# Python allows negative integers to be used as indices into a sequence, 
# such as a string. If string s has length n, and expression s[k] is used 
# for in- dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that 
# s[j] references the same element?

# Example:
# Input: arr[] =  {5, 7, 10, 5, 4, 1}
# positive index:  0  1  2   3  4  5
# negative index: -6 -5 -4  -3 -2 -1

arr = [5, 7, 10, 5, 4, 1]
print("Using negative indices to access list:")
for i in range(len(arr)):
    k = i - len(arr)
    print("Index:", k, ", Value:", arr[k])