# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
m = [[], _int_tensor([]), [1], _int_tensor([1]), [1, 2]]
self.assertFunctionMatchesEager(nested_for_loops, m)
