#Rotate Array 1,2,3,4,5,6,7  ->  7,6,5,1,2,3,4  | k=3
a=[1,2,3,4,5,6,7]
b=[]
k=3

for y in range(len(a)):
    print(y)

for x in range(len(a)):
    if(x<k):
        b.append(a[(len(a)-1)-x])
    else:
        b.append(a[x-k])

print("Original Array : ",a)
print("Rotate Array : ",b)
    