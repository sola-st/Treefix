# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/logical_expression_test.py
self.assertFunctionMatchesEager(composite_ors, False, True, False)
self.assertFunctionMatchesEager(composite_ors, False, False, False)
self.assertFunctionMatchesEager(composite_ands, True, True, True)
self.assertFunctionMatchesEager(composite_ands, True, False, True)
self.assertFunctionMatchesEager(composite_mixed, False, True, True)
self.assertFunctionMatchesEager(composite_ors_with_callable, False, True,
                                False)
self.assertFunctionMatchesEager(composite_ors_with_callable, False, False,
                                True)
self.assertFunctionMatchesEager(composite_ors_with_callable, False, False,
                                False)

self.assertFunctionMatchesEager(comparison, 1, 2, 3)
self.assertFunctionMatchesEager(comparison, 2, 1, 3)
self.assertFunctionMatchesEager(comparison, 3, 2, 1)
self.assertFunctionMatchesEager(comparison, 3, 1, 2)
self.assertFunctionMatchesEager(comparison, 1, 3, 2)
self.assertFunctionMatchesEager(comparison, 2, 3, 1)
