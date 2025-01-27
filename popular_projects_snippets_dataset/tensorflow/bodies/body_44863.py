# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers_test.py
with function_wrappers.FunctionScope(None, None,
                                     converter.STANDARD_OPTIONS):
    t = constant_op.constant(1)
self.assertEqual(self.evaluate(t), 1)
