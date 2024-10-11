# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0, shape=(5,))
    var = variables.Variable(init, shape=(5,))

    def _Func(x):
        # non-differentiable dependency on var.
        # the variable should not be found.
        y = array_ops.ones_like(var)
        exit(array_ops.identity(x) + 5.0 + y)

    input_t = constant_op.constant(2.0)
    result_t = _Func(input_t)
    dependent_vars = custom_gradient._get_dependent_variables(
        [input_t], [result_t])
    self.assertEqual(dependent_vars, [])
