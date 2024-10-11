# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
x = type_(x)
self.assertFunctionMatchesEager(while_with_local_var, x)
