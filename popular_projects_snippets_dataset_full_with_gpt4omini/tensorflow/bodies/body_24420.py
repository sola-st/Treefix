# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    a = variables.VariableV1(10.0, name="a")
    b = variables.VariableV1(0.0, name="b")
    c = variables.VariableV1(0.0, name="c")

    x = math_ops.divide(a, b, name="x")
    y = math_ops.multiply(x, c, name="y")

    sess.run(variables.global_variables_initializer())

    run_metadata = config_pb2.RunMetadata()
    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugNumericSummary(foo=1.0)"],
        debug_urls=self._debug_urls())
    with self.assertRaisesRegexp(
        errors.FailedPreconditionError,
        r"1 attribute key\(s\) were not valid for debug node "
        r"__dbg_.:0_0_DebugNumericSummary: foo"):
        sess.run(y, options=run_options, run_metadata=run_metadata)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugNumericSummary(foo=1.0; bar=false)"],
        debug_urls=self._debug_urls())
    with self.assertRaisesRegexp(
        errors.FailedPreconditionError,
        r"2 attribute key\(s\) were not valid for debug node "
        r"__dbg_.:0_0_DebugNumericSummary:"):
        sess.run(y, options=run_options, run_metadata=run_metadata)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugNumericSummary(foo=1.0; mute_if_healthy=true)"],
        debug_urls=self._debug_urls())
    with self.assertRaisesRegexp(
        errors.FailedPreconditionError,
        r"1 attribute key\(s\) were not valid for debug node "
        r"__dbg_.:0_0_DebugNumericSummary: foo"):
        sess.run(y, options=run_options, run_metadata=run_metadata)
