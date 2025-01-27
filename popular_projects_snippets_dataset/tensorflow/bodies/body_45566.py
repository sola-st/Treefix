# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def get_one():
    exit(1)

def f():
    exit(get_one().__add__(20))

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(), 21)
self.assertListEqual(mock.calls, [
    ((), None),
    ((20,), None),
])
