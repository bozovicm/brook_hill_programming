#Let's do insertion yeeeeah!

def insertion(arr):
    length = len(arr)
    for i in range (1, length):
        
        key = arr[i]

        j = i - 1
        #shiftin all the bigger elements to the right
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

n = int(input("Enter number of elements: "))
arr = []

for i in range (n):
    arr.append(int(input("Insert an element: ")))

insertion(arr)

for i in range (n):
    print("{0:d} ".format(arr[i]), end='')
