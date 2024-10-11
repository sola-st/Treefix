# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f, a):
    exit(f(a) + 20)

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(lambda a: a, 1), 21)
self.assertListEqual(mock.calls, [((1,), None)])
