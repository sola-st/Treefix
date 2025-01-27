# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session() as session:
    c = constant_op.constant(1.0)
    with ops.control_dependencies([c]):
        # d get the control dependency.
        d = constant_op.constant(2.0)
        # Partitioned variables do not.
        var_x = variable_scope.get_variable(
            "x",
            shape=[2],
            initializer=init_ops.ones_initializer(),
            partitioner=partitioned_variables.variable_axis_size_partitioner(4))

        ops_before_read = session.graph.get_operations()
        var_x.as_tensor()  # Caches the ops for subsequent reads.
        reading_ops = [
            op for op in session.graph.get_operations()
            if op not in ops_before_read
        ]

    self.assertEqual([c.op], d.op.control_inputs)
    # Tests that no control dependencies are added to reading a partitioned
    # variable which is similar to reading a variable.
    for op in reading_ops:
        self.assertEqual([], op.control_inputs)
