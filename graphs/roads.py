n = int(input("Enter the number of nodes in a graph: "))

matrix = []

total_length = 0

for i in range(n):
    row = [] 
    for j in range(n):
        row.append(int(input("Insert an element of an adjacency matrix: ")))
        if row[j] != -1:
            total_length = total_length + row[j]
    matrix.append(row)

"""for i in range(n):
    for j in range(n):
        print("{0:d} ".format(matrix[i][j]), end = "")
    print()"""

print ("Total cost is : {0:f} million dollars".format(total_length * 0.5))

# We have n cities which are representet as a weighted
# directed graph. If a cost of 1km of road is 0.5million usd
# find the total cost of the roads which are connecting these
# cities