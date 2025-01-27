# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f, g):
    exit(f(g() + 20) + 4000)

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(lambda x: x + 300, lambda: 1), 4321)
self.assertListEqual(mock.calls, [
    ((), None),
    ((21,), None),
])
