#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#Note:- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#Example
#s12:01:00PM'
#Return '12:01:00'.
#s12:01:00AM
#Return '00:01:00',
#Function Description
#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#timeConversion has the following parameter(s):
#• string s. a time in 12 hour format
#Returns
#• string, the time in 24 hour format
#Input Format
#A single strings that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).
#Constraints
#• All input times are valid
#Sample Input 0
#07:05:45PM
#Sample Output 0
#19:05:45


import math
import os
import random
import re
import sys
# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    if(s[-2:]=="AM"):
             if (s[:2]=="12"):
                  return "00"+s[2:-2]
             else:
                  return s[:-2]
    else:
          h=int(s[:2])
          if(h<12):
                 h+=12
                 return str(h)+s[2:-2]
    # Write your code here
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
