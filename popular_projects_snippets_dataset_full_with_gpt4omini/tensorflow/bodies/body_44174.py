# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/early_return_test.py
self.assertFunctionMatchesEager(
    raise_during_return_caught_in_tail_branch, type_(c))
