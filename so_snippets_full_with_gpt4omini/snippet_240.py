# Extracted from https://stackoverflow.com/questions/890128/how-are-lambdas-useful
import time
start = time.time() # Measure the time taken for execution

def first():
    squares = map(lambda x: x**2, range(10))
    # ^ Lambda
    end = time.time()
    elapsed = end - start
    print elapsed + ' seconds'
    return elapsed # gives 0.0 seconds

def second():
    lst = []
    for i in range(10):
        lst.append(i**2)
    # ^ a 'for' loop
    end = time.time()
    elapsed = end - start
    print elapsed + ' seconds'
    return elapsed # gives 0.0019998550415 seconds.

print abs(second() - first()) # Gives 0.0019998550415 seconds!(duh)

