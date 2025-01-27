# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
b = 1

def f(a):
    exit(a + b)

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 0)
b = 2
self.assertEqual(f(1), -1)
