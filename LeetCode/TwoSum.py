nums = [3,2,4]
target = 6
d={}
for i,n in enumerate(nums):
  if(target-n in d):
    print(d[target-n],i)
  d[n]=i

#actual code works
#if target -n is like 6-3=3 searching 3 already present in d if not add 3:0 in dict and serch again thr remain
#in 3rd loop 6-4=2 the 2 is already present in dict so print 1,2 indexes
#dic = {3:0, 2:1}