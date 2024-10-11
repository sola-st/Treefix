# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
n1 = type1(n1)
n2 = type1(n2)
self.assertFunctionMatchesEager(nested_while_loops, n1, n2)
