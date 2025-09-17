height = [9,8,6,2,5,4,8,3,7]
conVal=0
l=0
r=len(height)-1
gap=0
while(True):
  if height[l]<height[r]:
    gap=r-l
    if conVal>(height[l]*gap):
      conVal=gap*height[l]
    l=l+1
  else:
    gap=l-r
    if conVal>(height[r]*gap):
      conVal=gap*height[r]
    r=r-1
  if(l==r):
    break

print(-conVal)
