# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    u_init_val = np.array([[5.0, 3.0], [-1.0, 0.0]])
    v_init_val = np.array([[2.0], [-1.0]])

    # Use node names with overlapping namespace (i.e., parent directory) to
    # test concurrent, non-racing directory creation.
    u_name = "u"
    v_name = "v"
    w_name = "w"

    u_init = constant_op.constant(u_init_val, shape=[2, 2])
    u = variables.VariableV1(u_init, name=u_name)
    v_init = constant_op.constant(v_init_val, shape=[2, 1])
    v = variables.VariableV1(v_init, name=v_name)

    w = math_ops.matmul(u, v, name=w_name)

    u.initializer.run()
    v.initializer.run()

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_urls = "file://%s" % self._dump_root

    # Add debug tensor watch for u.
    debug_utils.add_debug_tensor_watch(
        run_options, "%s/read" % u_name, 0, debug_urls=debug_urls)
    # Add debug tensor watch for v.
    debug_utils.add_debug_tensor_watch(
        run_options, "%s/read" % v_name, 0, debug_urls=debug_urls)

    run_metadata = config_pb2.RunMetadata()

    # Invoke Session.run().
    sess.run(w, options=run_options, run_metadata=run_metadata)

    self.assertEqual(self._expected_partition_graph_count,
                     len(run_metadata.partition_graphs))

    dump = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)

simple_add_results = collections.namedtuple("SimpleAddResults", [
    "u_init_val", "v_init_val", "u", "v", "w", "u_name", "v_name", "w_name",
    "dump"
])
exit(simple_add_results(u_init_val, v_init_val, u, v, w, u_name, v_name,
                          w_name, dump))
