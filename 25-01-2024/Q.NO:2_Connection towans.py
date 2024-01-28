""Cities on a map are connected by a number of roads. The number of roads between each city is in an array and city 0 is the starting location. The number of roads from city 0 to city 1 is the first value in the array, from city 1 to city 2 is the second, and so on.
How many paths are there from city 0 to the last city in the list, modulo 1234567?
Example
n=4
routes = [3, 4, 5]
There are 3 roads to city 1, 4 roads to city 2 and 5 roads to city 3. The total number of roads is 3 x 4 x 5 mod 123456760.
Note
Pass all the towns T, for i=1 to n-1 in numerical order to reach Tn.
Function Description
Complete the connecting Towns function in the editor below.
connecting Towns has the following parameters:
int n; the number of towns
int routes[n-1]: the number of routes between towns
Returns
int: the total number of routes, modulo 1234567.
Input Format
The first line contains an integer T, T test-cases follow.
Each test-case has 2 lines.
The first line contains an integer N (the number of towns).
The second line contains N-1 space separated integers where the ith integer denotes the number of routes, N., from the town T; to Ti.1
Constraints
1 <= T<=1000
2< N <=100
1 <= routes[i] <=1000
Sample Input
2
3
13
4
222
Sample Output
3
8""

def connecting_towns(n, routes):
    paths = 1
    for i in range(n-1):
        paths *= routes[i] % 1234567
    return paths % 1234567

def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Number of towns
        routes = list(map(int, input().split()))  # Routes between towns
        result = connecting_towns(N, routes)
        print(result)

if _name_ == "_main_":
    main()
