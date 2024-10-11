# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
if context.executing_eagerly():
    var = resource_variable_ops.ResourceVariable(10, name="var")
else:
    var = variables.Variable(10)
result = math_ops.scalar_mul(3, var)
init = variables.global_variables_initializer()
with test_util.device(use_gpu=True):
    self.evaluate(init)
    self.assertEqual(30, self.evaluate(result))
