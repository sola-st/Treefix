# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    a = variables.VariableV1("1", name="a")
    b = variables.VariableV1("3", name="b")
    c = variables.VariableV1("2", name="c")

    d = math_ops.add(a, b, name="d")
    e = math_ops.add(d, c, name="e")
    n = parsing_ops.string_to_number(e, name="n")
    m = math_ops.add(n, n, name="m")

    sess.run(variables.global_variables_initializer())

    # Using DebugNumericSummary on sess.run(m) with the default
    # tolerate_debug_op_creation_failures=False should error out due to the
    # presence of string-dtype Tensors in the graph.
    run_metadata = config_pb2.RunMetadata()
    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugNumericSummary"],
        debug_urls=self._debug_urls())
    with self.assertRaises(errors.FailedPreconditionError):
        sess.run(m, options=run_options, run_metadata=run_metadata)

    # Using tolerate_debug_op_creation_failures=True should get rid of the
    # error.
    m_result, dump = self._debug_run_and_get_dump(
        sess, m, debug_ops=["DebugNumericSummary"],
        tolerate_debug_op_creation_failures=True)
    self.assertEqual(264, m_result)

    # The integer-dtype Tensors in the graph should have been dumped
    # properly.
    self.assertIn("n:0:DebugNumericSummary", dump.debug_watch_keys("n"))
    self.assertIn("m:0:DebugNumericSummary", dump.debug_watch_keys("m"))
