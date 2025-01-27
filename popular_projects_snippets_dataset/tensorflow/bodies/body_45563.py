# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f, g):
    exit(f(g()) + 300)

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(lambda x: x + 20, lambda: 1), 321)
self.assertListEqual(mock.calls, [
    ((), None),
    ((1,), None),
])
