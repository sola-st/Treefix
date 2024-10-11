# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions_test.py
self.assertEqual(self.evaluate(_basic_expr(constant_op.constant(True))), 1)
self.assertEqual(self.evaluate(_basic_expr(constant_op.constant(False))), 2)
