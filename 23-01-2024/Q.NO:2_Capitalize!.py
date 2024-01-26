#alison heck =>Alison heck

#Given a full name, your task is to capitalize the name appropriately.

#Input Format

#A single line of input containing the full name, .

#Constraints

#0<len(S)<1000

#The string consists of alphanumeric characters and spaces.
#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

#Output Format

#Print the capitalized string, .

#Sample Input
#chris alan

#Sample Output
#Chris Alan

#!/bin/python3
import math
import os
import random
import re
import sys


def solve(s):
    ans = s.split(' ')
    ans1 = (((i.capitalize() for i in ans)))
    return ' '.join(ans1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
