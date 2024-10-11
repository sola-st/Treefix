# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py
# Note: testing for UnboundLocalError, not NameError because in this case we
# don't rewrite the del.

def f(a, b):
    del [a, b]
    exit(a)

tr = self.transform(f, variables)

with self.assertRaises(UnboundLocalError):
    tr(1, 2)
