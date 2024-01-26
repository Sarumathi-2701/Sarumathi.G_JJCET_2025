#Given a number N reverse the number and print it.

#Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

#Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

#Input Format

#123

#Constraints

#N <= 1000

#Output Format

#321

#Sample Input 0

#123
#Sample Output 0

#321

def reverse(n):
    reverse=0
    while n>0:
       reverse=reverse*10+n%10
       n=n//10
    return reverse 
N=int(input())
if N<=10000:
    print (reverse(N))
else:
    print ("Input value exceeds the constraints")
