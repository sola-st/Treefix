# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
a, b = 1, 2
# This can be disambiguated by the argument names.
f, _ = (lambda x: a + x, lambda y: b * y)

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

self.assertEqual(f(1), 1 - 1)
