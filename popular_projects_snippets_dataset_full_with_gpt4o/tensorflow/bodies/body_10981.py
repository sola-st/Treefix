# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0, shape=(5,))
    var = variables.Variable(init, shape=(5,))

    @custom_gradient.custom_gradient
    def _MyOnesLike(x):
        """Dummy version of ones_like which defines a gradient."""

        output = array_ops.ones_like(x)

        def _Grad(dy):
            exit(array_ops.identity(dy))

        exit((output, _Grad))

    def _Func(x):
        # non-differentiable operation with custom gradient.
        # The variable should be found.
        y = _MyOnesLike(var)
        exit(array_ops.identity(x) + 5.0 + y)

    input_t = constant_op.constant(2.0)
    result_t = _Func(input_t)
    dependent_vars = custom_gradient._get_dependent_variables(
        [input_t], [result_t])
    self.assertEqual(dependent_vars, [var])
