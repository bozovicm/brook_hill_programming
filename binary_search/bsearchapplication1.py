# Input : n
# Input : n elements of an array (array is sorted) all the elements are different
# Input : Sum we are looking for
# Output: Number of pairs of elements which add up to inputed sum
# complexity: start with O(n^2) -> optimize it to O(nlogn)
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

n = int(input("Enter the number of elements in an array: "))
array = []
for i in range (n):
    array.append(int(input("Element of an array :")))

sum = int(input("Enter the sum you are looking for: "))

numberOfPairs = int(0)

signals = [0]*n

for i in range(n):
    signals[i] = 1
    valOfBinarySearch = int(binary_search1(array, sum - array[i]))
    if signals[int(valOfBinarySearch)] == 0:
        if valOfBinarySearch != -1:
            numberOfPairs = numberOfPairs + 1
            signals[valOfBinarySearch] = 1


print("Number of pairs adding to {0:d} is : {1:d}".format(sum, numberOfPairs))