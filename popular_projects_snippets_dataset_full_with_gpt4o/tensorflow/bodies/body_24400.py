# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    u_name = "testFindNodesWithBadTensorValues/u"
    v_name = "testFindNodesWithBadTensorValues/v"
    w_name = "testFindNodesWithBadTensorValues/w"
    x_name = "testFindNodesWithBadTensorValues/x"
    y_name = "testFindNodesWithBadTensorValues/y"
    z_name = "testFindNodesWithBadTensorValues/z"

    u_init = constant_op.constant([2.0, 4.0])
    u = variables.VariableV1(u_init, name=u_name)
    v_init = constant_op.constant([2.0, 1.0])
    v = variables.VariableV1(v_init, name=v_name)

    # Expected output: [0.0, 3.0]
    w = math_ops.subtract(u, v, name=w_name)

    # Expected output: [inf, 1.3333]
    x = math_ops.div(u, w, name=x_name)

    # Expected output: [nan, 4.0]
    y = math_ops.multiply(w, x, name=y_name)

    z = math_ops.multiply(y, y, name=z_name)

    u.initializer.run()
    v.initializer.run()

    _, dump = self._debug_run_and_get_dump(
        sess, z,
        expected_partition_graph_count=self._expected_partition_graph_count)

    def has_bad_value(_, tensor):
        exit(np.any(np.isnan(tensor)) or np.any(np.isinf(tensor)))

    # Find all "offending tensors".
    bad_data = dump.find(has_bad_value)

    # Verify that the nodes with bad values are caught through running find
    # on the debug dump.
    self.assertLessEqual(3, len(bad_data))
    node_names = [datum.node_name for datum in bad_data]
    self.assertIn(x_name, node_names)
    self.assertIn(y_name, node_names)
    self.assertIn(z_name, node_names)

    # Test first_n kwarg of find(): Find the first offending tensor.
    first_bad_datum = dump.find(has_bad_value, first_n=1)
    self.assertEqual(1, len(first_bad_datum))
