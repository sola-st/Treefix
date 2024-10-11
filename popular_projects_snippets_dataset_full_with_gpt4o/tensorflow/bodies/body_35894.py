# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session() as session:
    var_x = variable_scope.get_variable(
        "x",
        initializer=constant_op.constant([1., 2.]),
        partitioner=partitioned_variables.variable_axis_size_partitioner(4))

    c = constant_op.constant(1.0)
    with ops.control_dependencies([c]):
        ops_before_concat = session.graph.get_operations()
        value = var_x._concat()  # pylint: disable=protected-access
        concat_ops = [
            op for op in session.graph.get_operations()
            if op not in ops_before_concat
        ]

    concat_control_inputs = [
        ci for op in concat_ops for ci in op.control_inputs
    ]
    self.assertTrue(
        c.op in concat_control_inputs,
        "var_x._concat() should get control dependencies from its scope.")
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(value, var_x.as_tensor())
