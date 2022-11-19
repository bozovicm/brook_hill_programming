# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
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

n = int(input("Enter number of elements in a list: "))
elements = []

for i in range(n) :
    elements.append(int(input("Enter an element:")))

needle = int(input("Number you want to search: "))

indicator = int(binary_search1(elements, needle))

if indicator == -1 :
    print("Sorry, It's not there!")
else :
    print("WE FOUND IT! Index: {0:d}".format(indicator))