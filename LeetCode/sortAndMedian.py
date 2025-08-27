def sortIt(nums):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if(nums[i]>nums[j]):
        nums[i],nums[j] = nums[j],nums[i]
  return nums
    
nums1 = [1,2]
nums2 = [3,4]
median=0
sor_li = sortIt(nums1+nums2)
lenn=len(sor_li)
if (lenn%2!=0):
  print( sor_li[(lenn//2)] )
else: 
  print( ( sor_li[(lenn//2)-1]+sor_li[(lenn//2)] )/2  )
  
'''
if(len(sor_li)%2==0):
  pos= int( len(sor_li)/2 )
  median=(sor_li[pos-1]+sor_li[pos])/2
else:
  pos = int( len(sor_li)//2 )
  median = sor_li[pos]
  
print(pos,' ' ,median)
'''