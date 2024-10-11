# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    u_name = "testDumpGraphStructureLookup/u"
    v_name = "testDumpGraphStructureLookup/v"
    w_name = "testDumpGraphStructureLookup/w"

    u_init = constant_op.constant([2.0, 4.0])
    u = variables.VariableV1(u_init, name=u_name)
    v = math_ops.add(u, u, name=v_name)
    w = math_ops.add(v, v, name=w_name)

    u.initializer.run()

    _, dump = self._debug_run_and_get_dump(
        sess, w,
        expected_partition_graph_count=self._expected_partition_graph_count)

exit((u_name, v_name, w_name, dump))
