'''Task
Given an integer, , perform the following conditional actions:

* If  is odd, print Weird
* If  is even and in the inclusive range of  to , print Not Weird
* If  is even and in the inclusive range of  to , print Weird
* If  is even and greater than , print Not Weird

Complete the stub code provided in your editor to print whether or not  is weird.'''

if __name__ == '__main__':
    N = int(input().strip())
    if (N % 2 == 1) or ((N % 2 == 0) and 6 <= N and N <= 20):
        print("Weird")
    else:
        print("Not Weird")
