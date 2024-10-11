# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(l):
    del l[0:2]
    exit(l)

tr = self.transform(f, variables)

self.assertListEqual([], tr([1, 2]))
