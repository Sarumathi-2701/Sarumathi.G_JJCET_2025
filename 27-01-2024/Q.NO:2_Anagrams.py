#Two words are anagrams of one another if their letters can be rearranged to form the other word.
#Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.
#Example
#s = abccde
#Break s into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.
#Function Description
#Complete the anagram function in the editor below.
#anagram has the following parameter(s):
#⚫ string s: a string
#Return
•# int: the minimum number of characters to change or -1.
#Input Format
#The first line will contain an integer, q, the number of test cases.
#Each test case will contain a string 8.
#Constraints
#1≤g≤10
#18104#
⚫s c#onsists only of characters in the range ascii[a-z].
Sampl#e Input
#6
#aaabbb
#ab
#abc
#mnop
#xyyx
#Sample Output
##3
#1
#-1
#201


logic 1:
import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.


def anagram(s):
    length = len(s)
    # If the length of the string is odd, it's not possible to split into two equal substrings
    if length % 2 != 0:
        return -1
    mid = length // 2
    s1 = s[:mid]
    s2 = s[mid:]
    # Count the frequency of characters in each substring
    freq_s1 = [0] * 26
    freq_s2 = [0] * 26
    for char in s1:
        freq_s1[ord(char) - ord('a')] += 1
    for char in s2:
        freq_s2[ord(char) - ord('a')] += 1
    # Calculate the difference in character frequencies between the substrings
    changes_needed = 0
    for i in range(26):
        changes_needed += abs(freq_s1[i] - freq_s2[i])
        # The minimum number of c
anges is half of the total differences
    return changes_needed // 2
# Input
q = int(input().strip())
for _ in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)

logic 2:

def anagrams(s):
    n=len(s)
    if n%2==1:
        return -1
    s=Counter (s[:n//2])-Counter (s[n//2:])
    return sum(s,values())
