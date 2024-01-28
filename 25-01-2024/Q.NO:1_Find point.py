""Consider two points, p = (Px, Py) and q = (qz, qy). We consider the inversion or point reflection, r = (a, Ty), of point p across point q to be a 180° rotation of point p around 9.
Given n sets of points p and g, find for each pair of points and print two space- separated integers denoting the respective values of and ry on a new line.
Function Description
Complete the findPoint function in the editor below.
findPoint has the following parameters:
⚫int px, py, qx, qy: x and y coordinates for points p and q
Returns
• int[2]: x and y coordinates of the reflected point
Input Format
The first line contains an integer, n, denoting the number of sets of points. Each of then subsequent lines contains four space-separated integers that describe the respective values of Pr. Py, qz, and q, defining points p = (PP) and q = (qz, qy).
Constraints
• 1 ≤ n ≤15
•-100P, Py, qa qy≤ 100
Sample Input
2
6611
1122
Sample Output
#22 33
#Explanation""

logic 1:

def findPoint(px, py, qx, qy):
    rx = 2 * qx - px
    ry = 2 * qy - py
    return [rx, ry]

def main():
    n = int(input())
    
    for _ in range(n):
        px, py, qx, qy = map(int, input().split())
        reflected_point = findPoint(px, py, qx, qy)
        print(*reflected_point)

if _name_ == "_main_":
    main()
logic 2:

n=int(input())

for i in range(n):

   px,py,qx,qy=map(int,input().split ())

   print(2*qx-px,2*qy-px)

