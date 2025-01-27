# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(a, b, c):
    del a, b, c[0]
    a = 1
    exit((a, b, c))

tr = self.transform(f, variables)

with self.assertRaisesRegex(NameError, "'b' is used before assignment"):
    tr(1, 2, [1, 2])
