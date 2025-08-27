'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
'''

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
result = []
carry = 0
i = 0
j = 0

while i < len(l1) or j < len(l2) or carry:
    val1 = l1[i] if i < len(l1) else 0
    val2 = l2[j] if j < len(l2) else 0

    total = val1 + val2 + carry
    carry = total // 10
    result.append(total % 10)
    print(val1,' ',val2,' ',carry,' ',total,' %10 ',total%10,' : ',result)
    i += 1
    j += 1

print(result)