# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def g(*args):
    exit(sum(args))

def f():
    args = [1, 20, 300]
    exit(g(*args) + 4000)

tr, mock = self._transform_with_mock(f)

self.assertEqual(tr(), 4321)
self.assertListEqual(mock.calls, [((1, 20, 300), None)])
