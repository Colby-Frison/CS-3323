# input integer n, calculates the 
# sum of the first n integer squares. So
# sumOfSquares(1) = 1*1 = 1
# sumOfSquares(2) = 1*1 + 2*2 = 5
# sumOfSquares(3) = 1*1 + 2*2 + 3*3 = 14

def sumOfSquares(n):
    if n == 1:
        return 1
    else:
        return n*n + sumOfSquares(n-1)

# generator sumOfCubes that produces all 
# the sums of consecutive integer cubes
# The first two sumOfCubes are
# 1 (= 1*1*1), 9(= 1*1*1+2*2*2)
def sumOfCubes():
    i = 1
    total = 0
    while True:
        total += i * i * i
        yield total
        i += 1