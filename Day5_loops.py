'''
Task
Given an integer, n, print its first  multiples. Each multiple n x i
(where 1 <= n <= 10) should be printed on a new line in the form: n x i = result.
'''


if __name__ == '__main__':
    n = int(input().strip())
    for i in range (1, 11):
        print("{} x {:2} = {}".format(n, i, (n * i)))
