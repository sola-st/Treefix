# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def g(a, b, c, d):
    exit(a * 1000 + b * 100 + c * 10 + d)

def f():
    args1 = (1,)
    args2 = [3]
    exit(g(*args1, 2, *args2, 4))

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(), 1234)
self.assertListEqual(mock.calls, [((1, 2, 3, 4), None)])
