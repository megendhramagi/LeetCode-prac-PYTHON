#need to modify wrong outputs
numList=[]

print("Enter any 5 numbers : ")
for x in range(5):
    numList.append(int(input("> ")))

print("Before Sorting : ",numList)
for x in range(len(numList)-1):
    if(numList[x]>numList[x+1]):
        temp=numList[x]
        numList[x]=numList[x+1]
        numList[x+1]=temp
print("After Swapping : ",numList)