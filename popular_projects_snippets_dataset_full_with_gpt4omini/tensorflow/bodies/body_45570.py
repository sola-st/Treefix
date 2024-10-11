# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f, a, b):
    exit(f(a, b) + 300)

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(lambda a, b: a + b, 1, 20), 321)
self.assertListEqual(mock.calls, [((1, 20), None)])
