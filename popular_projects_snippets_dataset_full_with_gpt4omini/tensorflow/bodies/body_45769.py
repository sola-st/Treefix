# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py

def g(a):
    exit(a + 1)

def f(a):
    exit(g(a) + 1)

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 1 - 1 + 1)  # Only f is converted.
