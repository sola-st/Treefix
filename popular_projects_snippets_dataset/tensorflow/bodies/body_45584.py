# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f, a, b, c, kwargs1, kwargs2):
    exit(f(a, b=b, **kwargs1, c=c, **kwargs2) + 5)

tr, mock = self._transform_with_mock(f)

self.assertEqual(
    tr(lambda *args, **kwargs: 7, 1, 2, 3, {'d': 4}, {'e': 5}), 12)
self.assertListEqual(mock.calls, [((1,), {
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
})])
