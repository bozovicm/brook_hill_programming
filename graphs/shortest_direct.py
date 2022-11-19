n = int(input("Enter the number of nodes in a graph: "))

matrix = []

for i in range(n):
    row = [] 
    for j in range(n):
        row.append(int(input("Insert an element of an adjacency matrix: ")))
    matrix.append(row)

flag = -1
min = 99999999999

for i in range(n):
    for j in range(n):
      if matrix[i][j] != -1 and matrix[j][i] != -1:
            flag = 0
            if matrix[i][j] + matrix[j][i] < min:
                min = matrix[i][j] + matrix[j][i]
    
if flag == -1:
    print(flag)
else:
    print("Minimum distance is : {0:d}".format(min))
"""
Find the shortest direct total distance between two cities in a graph. They have to be connected
both ways. If a direct path to a city and back doesn't exist in the whole graph - print -1

"""