# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f):
    exit(f() + 20)

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(lambda: 1), 21)
self.assertListEqual(mock.calls, [((), None)])
