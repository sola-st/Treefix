# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
"""Test watching output slots not attached to any outgoing edges."""

with session.Session(config=no_rewrite_session_config()) as sess:
    u_init_val = np.array([[5.0, 3.0], [-1.0, 0.0]])
    u = constant_op.constant(u_init_val, shape=[2, 2], name="u")

    # Create a control edge from a node with an output: From u to z.
    # Node u will get executed only because of the control edge. The output
    # tensor u:0 is not attached to any outgoing edge in the graph. This test
    # checks that the debugger can watch such a tensor.
    with ops.control_dependencies([u]):
        z = control_flow_ops.no_op(name="z")

    _, dump = self._debug_run_and_get_dump(sess, z)

    # Assert that the DebugIdentity watch on u works properly.
    self.assertEqual(1, len(dump.dumped_tensor_data))
    datum = dump.dumped_tensor_data[0]
    self.assertEqual("u", datum.node_name)
    self.assertEqual(0, datum.output_slot)
    self.assertEqual("DebugIdentity", datum.debug_op)
    self.assertAllClose([[5.0, 3.0], [-1.0, 0.0]], datum.get_tensor())
