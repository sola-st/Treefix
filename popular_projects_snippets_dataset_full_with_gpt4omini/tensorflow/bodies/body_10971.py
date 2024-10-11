# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    var_name = "my_variable"
    v_z = variable_scope.get_variable(var_name, shape=())
    v_o = variable_scope.get_variable(var_name + "_ones", shape=())

    # The variable is closed over. It should be found.
    func = lambda x: array_ops.identity(x) + 5.0 + v_z + v_o

    input_t = constant_op.constant(2.0)
    result_t = func(input_t)
    dependent_vars = custom_gradient._get_dependent_variables(
        [input_t], [result_t])
    self.assertEqual(set(dependent_vars), set([v_o, v_z]))
