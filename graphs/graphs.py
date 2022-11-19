n = int(input("Enter the number of nodes in a graph: "))

matrix = []

for i in range(n):
    row = [] 
    for j in range(n):
        row.append(int(input("Insert an element of an adjacency matrix: ")))
    matrix.append(row)



for i in range(n):
    for j in range(n):
        print("{0:d} ".format(matrix[i][j]), end = "")
    print()
    

# We have n cities which are representet as a weighted
# directed graph. If a cost of 1km of road is 0.5million usd
# find the total cost of the roads which are connecting these
# cities