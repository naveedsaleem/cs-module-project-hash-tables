# Your code here
import random
import math
import time

lookup_table = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if (x, y) not in lookup_table:
        lookup_table[(x, y)] = slowfun_too_slow(x, y)
    return lookup_table[(x, y)]



start_time = time.time()
# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')  
end_time = time.time()
print(end_time - start_time)  


