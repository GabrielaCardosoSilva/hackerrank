
import math
import os
import random
import re
import sys

def reverse (arr):
        newArr = arr[::-1]
        return print(*newArr, sep =' ')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    reverse(arr)
