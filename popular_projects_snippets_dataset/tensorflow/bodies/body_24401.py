# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    u_name = "testFindInfOrNanWithOpNameExclusion/u"
    v_name = "testFindInfOrNanWithOpNameExclusion/v"
    w_name = "testFindInfOrNanWithOpNameExclusion/w"
    x_name = "testFindInfOrNanWithOpNameExclusion/x"
    y_name = "testFindInfOrNanWithOpNameExclusion/y"
    z_name = "testFindInfOrNanWithOpNameExclusion/z"

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

    # Find all "offending tensors".
    bad_data = dump.find(debug_data.has_inf_or_nan,
                         exclude_node_names=".*/x$")

    # Verify that the nodes with bad values are caught through running find
    # on the debug dump.
    self.assertLessEqual(2, len(bad_data))
    # Assert that the node `x` should have been excluded.
    node_names = [datum.node_name for datum in bad_data]
    self.assertIn(y_name, node_names)
    self.assertIn(z_name, node_names)

    first_bad_datum = dump.find(
        debug_data.has_inf_or_nan, first_n=1, exclude_node_names=".*/x$")
    self.assertEqual(1, len(first_bad_datum))
