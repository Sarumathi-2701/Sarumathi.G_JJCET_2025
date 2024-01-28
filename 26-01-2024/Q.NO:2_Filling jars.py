""Animesh has n empty candy jars, numbered from 1 to n, with infinite capacity. He performs m operations. Each operation is described by 3 integers, a, b, and k. Here, a and b are indices of the jars, and k is the number of candies to be added inside each jar whose index lies between a and b (both inclusive). Can you tell the average number of candies. after m operations?
Example
n=5 operations =[[1,2,10],[3,5,10]]
The array has 5 elements that all start at 0. In the first operation, add 10 to the first 2 elements. Now the array is [10, 10, 0, 0, 0]. In the second operation, add 10 to the last 3 elements (3-5). Now the array is [10, 10, 10, 10, 10] and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.
Function Description
Complete the solve function in the editor below.
solve has the following parameters:
• int n: the number of candy jars
• int operations[m][3]: a 2-dimensional array of operations
Returns
• int: the floor of the average number of canidies in all jars
Input Format
The first line contains two integers, n and m, separated by a single space. m lines follow. Each of them contains three integers, a, b, and k, separated by spaces.
Constraints
3\le n\le10^{7}
1\le m\le10^{5}
1\le a\le b\le N
0\le k\le10^{6}
Sample Input
STDIN
53
1 2 100
2 5 100
3 4 100
Function
n=5. operations[] size = 3 operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
Sample Output
160""


def solve(n, operations):
    total_candies = 0
    for operation in operations:
        start_index, end_index, candies_added = operation
        total_candies += (end_index - start_index + 1) * candies_added
    average_candies = total_candies // n
    return average_candies
n, m = map(int, input().split())
operations = []
for _ in range(m):
    operation = list(map(int, input().split()))
    operations.append(operation)
result = solve(n, operations)
print(result)
