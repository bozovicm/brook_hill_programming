#LET'S CODE BUBBLE SORT!!!!!

def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


    # 1 2 3 4 5

    # 5 4 3 2 1
    # 5 4 3 1 2
    # 5 4 1 3 2
    # 5 1 4 3 2
    # 1 5 4 3 2

    # 

    # swap (arr[0], arr[3])
    # 4 2 3 1 5

def bubble(arr):

    flag = False
    length = len(array) #if we call function len in a loop (this function also a loop) we get n * actual complexity 
    for i in range (length):

        for j in range (0, length - 1 - i):

            if arr[j] > arr[j + 1]:
                flag = True
                #arr[j], arr[j+1] = arr[j + 1], arr[j]
                swap (arr, j, j+1)

        if not flag:
            return

n = int(input("Enter number of elements: "))
array = []
for i in range(n):
    array.append(int(input("Enter an element: ")))

bubble(array)

for i in range (n):
    print("{0:d} ".format(array[i]), end='')