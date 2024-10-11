# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
m = type_(m)
self.assertFunctionMatchesEager(nested_for_loops, m)
