# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.any_([False, True, False]), True)
self.assertEqual(py_builtins.any_([False, False, False]), False)
