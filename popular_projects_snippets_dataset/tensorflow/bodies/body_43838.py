# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
l = type_(l)
self.assertFunctionMatchesEager(for_creates_var, l)
