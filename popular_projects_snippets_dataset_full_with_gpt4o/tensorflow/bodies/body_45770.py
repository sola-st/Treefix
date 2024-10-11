# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
b = 2
f = lambda x: (b + (x if x > 0 else -x))

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 2 - 1)
self.assertEqual(f(-1), 2 - 1)

b = 3

self.assertEqual(f(1), 3 - 1)
self.assertEqual(f(-1), 3 - 1)
