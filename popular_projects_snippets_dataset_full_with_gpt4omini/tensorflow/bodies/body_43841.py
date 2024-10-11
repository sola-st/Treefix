# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
l1 = type1(l1)
l2 = type1(l2)
self.assertFunctionMatchesEager(successive_for_loops, l1, l2)
