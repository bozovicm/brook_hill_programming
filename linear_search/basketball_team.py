# We have a basketball team's results
# during a season in an integer array
# we have elements equal to either 1 or a 0
# 1 represents a victory 0 represents a loss
# find the longest consecutive series of victories

# 011001110101111100110

# index 0 current value = 0 , max value = 0 
# index 1 current value = 1, max value = 1
# index 2 current value = 1, max value = 2
# index 3 current value = 0, max value = 2
# index 4 current value = 0, max value = 2
# index 5 current value = 1, max value = 2
# index 6 current value = 2, max value = 2
# index 7 current value = 3, max value = 3
# ... etc

n = int(input("Number of games: "))
results = []
for i in range (n):
    results.append(int(input()))
current = int(0) #current value of consecutive wins in an array
max = int(0) #maximum value of wins

for i in range (n):
    if results[i] == 1:
        for j in range (i, n):
            if (results[j] == 1):
                current = current + 1
                if (max < current):
                    max = current
            else:
                i = i + current
                current = 0
print(max)
