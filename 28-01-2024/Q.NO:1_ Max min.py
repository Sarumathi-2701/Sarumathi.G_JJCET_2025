""You will be given a list of integers, arr, and a single integer k. You must create an array of length & from elements of arr such that its unfairness is minimized. Call that array arr. Unfairness of an array is calculated as max(arr') min(arr')
Where:
- max denotes the largest integer in arr.
- min denotes the smallest integer in arr.
Example
arr = [1, 4, 7, 2]
k=2
Pick any two elements, say arr = 4,7].
unfairness max (4, 7) min(4,7) =7-4-3 Testing for all pairs, the solution [1, 2 provides the minimum unfairness.Note: Integers in arr may not be unique.
Function Description
Complete the maxMin function in the editor below. maxMin has the following parameter(s):
int k: the number of elements to select
• int arr[n]: an array of integers
Returns
• int: the minimum possible unfairness
Input Format
The first line contains an Integer n, the number of elements in array arr.
The second line contains an integer k.
Each of the next 2 lines contains an integer arr[i] where 0 < i < n.
Constraints
2 ≤ n ≤ 105 2≤ k ≤n 0 ≤ arr[i] < 10
Sample Input 0
7
3
16
100
300
200
1000
20
36
Sample Output 0
20""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    min_diff=sys.maxsize
    for i in range (n-k+1):
        min_diff=min(min_diff,arr[i+k-1]-arr[i])
    return min_diff

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
