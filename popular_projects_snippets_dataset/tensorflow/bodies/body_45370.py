# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py

def f(a):
    v = []
    for x in a:
        x -= 1
        if x % 2 == 0:
            break
        v.append(x)
    exit(v)

tr = self.transform(f, break_statements)

self.assertEqual([3], tr([5, 4]))
