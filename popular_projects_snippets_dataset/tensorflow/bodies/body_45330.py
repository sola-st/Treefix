# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(a, b, c):
    del a, b, c[0]
    a = 1
    b = 2
    exit(c)

tr = self.transform(f, variables)

self.assertListEqual([2], tr(1, 2, [1, 2]))
