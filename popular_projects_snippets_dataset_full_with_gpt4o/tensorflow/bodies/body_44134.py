# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
self.assertFunctionMatchesEager(if_creates_var, True)
self.assertFunctionMatchesEager(else_creates_var, False)
self.assertFunctionMatchesEager(if_destroys_var, False)
self.assertFunctionMatchesEager(else_destroys_var, True)
