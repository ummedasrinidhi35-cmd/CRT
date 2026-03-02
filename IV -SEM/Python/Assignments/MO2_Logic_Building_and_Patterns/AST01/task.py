def isUgly(self, n: int) -> bool:
    if n <= 0:
        return False
    
    # Divide n by 2, 3, and 5 as long as possible
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    
    # If n becomes 1, it is an ugly number
    return n == 1



if __name__ == '__main__':
    n = int(input())
    print(isUgly(n))
