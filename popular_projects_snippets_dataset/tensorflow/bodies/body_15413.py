# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
x = ragged_factory_ops.constant([[1, 2], [3, 4, 5]])
v = variables.Variable(10)
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(math_ops.add(x, v), [[11, 12], [13, 14, 15]])
