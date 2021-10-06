''''
Task
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Example
A = [1, 2, 3, 4]
Print 4 3 2 1. Each integer is separated by one space.

Input Format

The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers that describe array A's elements.
'''

def reverse (arr):
        newArr = arr[::-1]
        return print(*newArr, sep =' ')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    reverse(arr)
