# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    func = lambda x: array_ops.identity(x) + 5.0
    input_t = constant_op.constant(2.0)
    result_t = func(input_t)
    dependent_vars = custom_gradient._get_dependent_variables(
        [input_t], [result_t])

    # There are no variables.
    self.assertEqual(dependent_vars, [])
