n = int(input("Enter number of elements: "))
elements = []
for i in range(n) :
    elements.append(int(input()))
needle = int(input("Enter the needle: ")) 
indicator = -1
for i in range (n):
    if elements[i] == needle:
        indicator = i

if indicator != -1 :
    print("WE FOUND IT, INDEX IS: %d"%(indicator))
else :
    print("WE DID NOT FIND IT :(")