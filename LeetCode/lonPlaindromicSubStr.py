'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

in: ac
out: a
'''


s='baac'
i=1
res=''
while(i<=(len(s))):
  #print('++++++++++++++++')
  for j in range(0,i):
    ts=s[j:len(s)+(j-i+1)]
    rts=ts[::-1]
    #print(j,i,'ts : ',ts,'| rts : ',rts,' ;;',len(s)+(j-i+1))
    if(ts==rts):
      res=ts
      break
  if(res!=''):
    break
  i=i+1
print(": ",res)