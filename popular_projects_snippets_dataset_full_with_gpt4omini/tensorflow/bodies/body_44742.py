# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.all_([False, True, False]), False)
self.assertEqual(py_builtins.all_([True, True, True]), True)
