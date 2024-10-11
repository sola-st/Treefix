# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers_test.py
v = variables.Variable(1)
with function_wrappers.FunctionScope(
    '_', None,
    converter.ConversionOptions(
        optional_features=converter.Feature.AUTO_CONTROL_DEPS)) as scope:
    v.assign(2)
    op = scope.ret(constant_op.constant(1), True)
self.evaluate(op)
self.assertEqual(self.evaluate(v.read_value()), 2)
