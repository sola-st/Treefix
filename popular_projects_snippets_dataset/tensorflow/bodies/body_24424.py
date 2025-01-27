# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    u_init = constant_op.constant(10.0)
    u = variables.VariableV1(u_init, name="traceback/u")
    v_init = constant_op.constant(20.0)
    v = variables.VariableV1(v_init, name="traceback/v")

    w = math_ops.multiply(u, v, name="traceback/w")

    sess.run(variables.global_variables_initializer())
    _, dump = self._debug_run_and_get_dump(sess, w)

    # Prior to setting the Python graph, attempts to do traceback lookup
    # should lead to exceptions.
    with self.assertRaisesRegexp(
        LookupError, "Python graph is not available for traceback lookup"):
        dump.node_traceback("traceback/w")

    dump.set_python_graph(sess.graph)

    # After setting the Python graph, attempts to look up nonexistent nodes
    # should lead to exceptions.
    with self.assertRaisesRegexp(KeyError,
                                 r"Cannot find node \"foo\" in Python graph"):
        dump.node_traceback("foo")

    # Lookup should work with node name input.
    traceback = dump.node_traceback("traceback/w")
    self.assertIsInstance(traceback, tuple)
    self.assertGreater(len(traceback), 0)
    for trace in traceback:
        self.assertIsInstance(trace, tuple)

    # Lookup should also work with tensor name input.
    traceback = dump.node_traceback("traceback/w:0")
    self.assertIsInstance(traceback, tuple)
    self.assertGreater(len(traceback), 0)
    for trace in traceback:
        self.assertIsInstance(trace, tuple)
