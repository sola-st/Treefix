# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
b = 2

def f(x):
    g = lambda x: b + x
    exit(g(x))

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 2 - 1)
