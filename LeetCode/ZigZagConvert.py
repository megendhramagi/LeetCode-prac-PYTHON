strr="PAYPALISHIRING"
k=0
nr=4
n=0
li=[[]for _ in range(nr)]
while(k<len(strr)):
  if(n<nr):
    li[n].append(strr[k])
    print('k : ',k,' n: ',n,' li: ',li)
    n=n+1
    k=k+1
  else:
    for i in range((n-2),-1,-1):
      li[i].append(strr[k])
      print(' i: ',i,' k: ',k,' n: ',n,' li: ',li)
      k=k+1
    n=1
zigzag = ''.join(item for sub in li for item in sub)

print(li)
print(zigzag)
      
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 
'''