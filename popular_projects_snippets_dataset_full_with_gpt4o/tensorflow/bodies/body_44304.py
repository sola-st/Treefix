# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions_test.py
self.assertEqual(self.evaluate(_basic_expr(True)), 1)
self.assertEqual(self.evaluate(_basic_expr(False)), 2)
self.assertEqual(
    conditional_expressions.if_exp(True, lambda: 1, lambda: 2, ''), 1)
self.assertEqual(
    conditional_expressions.if_exp(False, lambda: 1, lambda: 2, ''), 2)
