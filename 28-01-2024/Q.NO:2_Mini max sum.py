""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Example
атт = [1, 3, 5, 7, 9]
The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. The function prints
16 24
Function Description
Complete the miniMaxSum function in the editor below.
miniMaxSum has the following parameter(s):
• arr: an array of 5 integers
Print
Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.
Input Format
A single line of five space-separated integers.
Constraints
1 ≤ arr[i] < 109
Output Format
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
Sample Input
12345
Sample Output
10 14""

logic 1:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
   s = 0
   minnum = 9999999999999
   maxnum = 0
   n = len(arr)
   for i in range(n):
       s += arr[i]
       minnum = min(minnum, arr[i])
       maxnum = max(maxnum, arr[i])
   print(s-maxnum, s-minnum)
    # Write your code here
if _name_ == '_main_':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)


logic 2:


import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)

# Input
arr = list(map(int, input().split()))

# Function Call
miniMaxSum(arr)
