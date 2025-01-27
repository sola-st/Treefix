# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
b = 2
c = 1

def f(a, d=c + 1):
    exit(a + b + d)

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 1 - 2 - 2)
c = 0
self.assertEqual(f(1), 1 - 2 - 2)  # Defaults are evaluated at definition.
b = 1
self.assertEqual(f(1), 1 - 2 - 1)
