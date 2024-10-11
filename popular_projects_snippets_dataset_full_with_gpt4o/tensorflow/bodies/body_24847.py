# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_file_test.py
"""Test watching different tensors on different runs of the same graph."""

with session.Session(
    config=session_debug_testlib.no_rewrite_session_config()) as sess:
    u_init_val = [[5.0, 3.0], [-1.0, 0.0]]
    v_init_val = [[2.0], [-1.0]]

    # Use node names with overlapping namespace (i.e., parent directory) to
    # test concurrent, non-racing directory creation.
    u_name = "diff_Watch/u"
    v_name = "diff_Watch/v"

    u_init = constant_op.constant(u_init_val, shape=[2, 2])
    u = variables.VariableV1(u_init, name=u_name)
    v_init = constant_op.constant(v_init_val, shape=[2, 1])
    v = variables.VariableV1(v_init, name=v_name)

    w = math_ops.matmul(u, v, name="diff_Watch/matmul")

    u.initializer.run()
    v.initializer.run()

    for i in range(2):
        run_options = config_pb2.RunOptions(output_partition_graphs=True)

        run_dump_root = self._debug_dump_dir(run_number=i)
        debug_urls = self._debug_urls(run_number=i)

        if i == 0:
            # First debug run: Add debug tensor watch for u.
            debug_utils.add_debug_tensor_watch(
                run_options, "%s/read" % u_name, 0, debug_urls=debug_urls)
        else:
            # Second debug run: Add debug tensor watch for v.
            debug_utils.add_debug_tensor_watch(
                run_options, "%s/read" % v_name, 0, debug_urls=debug_urls)

        run_metadata = config_pb2.RunMetadata()

        # Invoke Session.run().
        sess.run(w, options=run_options, run_metadata=run_metadata)

        self.assertEqual(self._expected_partition_graph_count,
                         len(run_metadata.partition_graphs))

        dump = debug_data.DebugDumpDir(
            run_dump_root, partition_graphs=run_metadata.partition_graphs)
        self.assertTrue(dump.loaded_partition_graphs())

        # Each run should have generated only one dumped tensor, not two.
        self.assertEqual(1, dump.size)

        if i == 0:
            self.assertAllClose([u_init_val],
                                dump.get_tensors("%s/read" % u_name, 0,
                                                 "DebugIdentity"))
            self.assertGreaterEqual(
                dump.get_rel_timestamps("%s/read" % u_name, 0,
                                        "DebugIdentity")[0], 0)
        else:
            self.assertAllClose([v_init_val],
                                dump.get_tensors("%s/read" % v_name, 0,
                                                 "DebugIdentity"))
            self.assertGreaterEqual(
                dump.get_rel_timestamps("%s/read" % v_name, 0,
                                        "DebugIdentity")[0], 0)
