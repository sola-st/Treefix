# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
self.assertFunctionMatchesEager(if_returns_none, True)
self.assertFunctionMatchesEager(if_else_returns_none, False)
self.assertFunctionMatchesEager(else_returns_none, False)
