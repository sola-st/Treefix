# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
iterator = iter([1, 2, 3])
self.assertEqual(py_builtins.next_(iterator), 1)
self.assertEqual(py_builtins.next_(iterator), 2)
self.assertEqual(py_builtins.next_(iterator), 3)
with self.assertRaises(StopIteration):
    py_builtins.next_(iterator)
self.assertEqual(py_builtins.next_(iterator, 4), 4)
