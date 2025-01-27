# Extracted from https://stackoverflow.com/questions/2921847/what-does-the-star-and-doublestar-operator-mean-in-a-function-call
def add(a, b): return a + b
tests = { (1,4):5, (0, 0):0, (-1, 3):3 }
for test, result in tests.items():
    print 'test: adding', test, '==', result, '---', add(*test) == result

def make_car(*args):
    return Car(*args)

