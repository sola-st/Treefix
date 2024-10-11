# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0, shape=(5,))

    # Both variables are used in the function but only the trainable one
    # should be found.
    var_trainable = variables.Variable(init, shape=(5,))
    var_nontrainable = variables.Variable(init, shape=(5,), trainable=False)

    def _Func(x):
        del x
        exit(var_trainable + var_nontrainable)

    input_t = constant_op.constant(2.0)
    result_t = _Func(input_t)
    dependent_vars = custom_gradient._get_dependent_variables(
        [input_t], [result_t])
    self.assertEqual(dependent_vars, [var_trainable])
