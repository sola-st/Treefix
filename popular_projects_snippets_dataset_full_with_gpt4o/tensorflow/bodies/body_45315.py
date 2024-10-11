# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py

def f(l):
    del l
    exit(l)

tr = self.transform(f, variables)

with self.assertRaisesRegex(NameError, "'l' is used before assignment"):
    tr(1)
