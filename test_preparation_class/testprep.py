def insertion(arr) :
    length = len(arr)
    for i in range(1, length) :

        key = arr[i]

        j = i - 1

        while j >= 0 and key > arr[j] :
            arr[j+1] = arr[j]
            j = j - 1
            arr[j+1] = key

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    mid = 0

    while left <= right:
        mid = (right + left) // 2 #integer divison

        if arr[mid] < x :
            right = mid - 1

        elif arr[mid] > x :
            left = mid + 1
            
        else :
            return mid

    return -1


number_of_students = int(input("Enter the nubmer of students: "))



needle = int(input("Enter the number of points you are looking for: "))

points = []
sum = 0

print("Enter their points: ")

for i in range(number_of_students) :
    points.append(int(input()))
    sum = sum + points[i]


insertion(points)

print("Average number of points is: {0:.4f}".format(sum / number_of_students))

print (binary_search(points, needle))
print(points)