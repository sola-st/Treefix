# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/logical_expression_test.py
self.assertFunctionMatchesEager(equality, 1, 1)
self.assertFunctionMatchesEager(equality, 1, 2)
self.assertFunctionMatchesEager(inequality, 1, 1)
self.assertFunctionMatchesEager(inequality, 1, 2)
self.assertFunctionMatchesEager(multiple_equality, 1, 1, 2)
self.assertFunctionMatchesEager(multiple_equality, 1, 1, 1)
