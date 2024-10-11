# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def f(f, a, *args, **kwargs):
    exit(f(a, *args, **kwargs) + 5)

tr, mock = self._transform_with_mock(f)

self.assertEqual(
    tr(lambda *args, **kwargs: 7, 1, *[2, 3], **{
        'b': 4,
        'c': 5
    }), 12)
self.assertListEqual(mock.calls, [((1, 2, 3), {'b': 4, 'c': 5})])
