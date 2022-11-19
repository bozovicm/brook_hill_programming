# check if there is an element in a sorted array which has the same value as its index
# for example : -1 1 7 8 9 23 89 117 - array[1] = 1 so it exists
# complexity: start with O(n) and finish with O(logn)

def binary_search1(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

n = int(input("Enter the number of elements: "))

array = []

for i in range (n):
    array.append(int(input("Enter an element: ")))
    array[i] = array[i] - i

indicator = -1

indicator = binary_search1(array, 0)

"""
for i in range (n):
    if array[i] == i:
        indicator = i
        break
    linear search
"""

if indicator != -1:
    print("We found it! It's element {0:d} at the index {0:d}".format(indicator))
else:
    print("It's not there :(")
