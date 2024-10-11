# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
l = type_(l)
self.assertFunctionMatchesEager(for_with_local_var, l)
