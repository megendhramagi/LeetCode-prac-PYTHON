'''
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

def reverseIt(num):
  summ=0
  while(True):
    if(num==0):break
    rem=num%10
    num=num//10
    summ=summ*10+rem
  return summ

num=-122

if(num<0):
  num= reverseIt(num*-1) * -1
elif(num>0):
  num= reverseIt(num)

print(num)


