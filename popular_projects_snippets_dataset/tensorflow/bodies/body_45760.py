# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
def f(a):
    exit(a + 1)

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 0)
