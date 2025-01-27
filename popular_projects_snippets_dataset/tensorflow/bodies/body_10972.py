# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    init = constant_op.constant(100.0)
    var = variables.Variable(init)

    # The variable is d-separated by the inputs. It should not be found.
    input_t = array_ops.identity(var) * 5.0

    func = lambda x: array_ops.identity(x) + 5.0
    result_t = func(input_t)
    dependent_vars = custom_gradient._get_dependent_variables(
        [input_t], [result_t])
    self.assertEqual(dependent_vars, [])
