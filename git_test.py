import numpy as np

def is_prime(n: int) -> bool:
    if n == 1:
        return False
    else:
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
