# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
"""Test the debug tensor dumping when error occurs in graph runtime."""

with session.Session() as sess:
    ph = array_ops.placeholder(dtypes.float32, name="mismatch/ph")
    x = array_ops.transpose(ph, name="mismatch/x")
    m = constant_op.constant(
        np.array(
            [[1.0, 2.0]], dtype=np.float32), name="mismatch/m")
    y = math_ops.matmul(m, x, name="mismatch/y")

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugIdentity"],
        debug_urls=self._debug_urls())

    with self.assertRaises(errors.OpError):
        sess.run(y,
                 options=run_options,
                 feed_dict={ph: np.array([[-3.0], [0.0]])})

    dump = debug_data.DebugDumpDir(self._dump_root)

    self.assertGreaterEqual(dump.core_metadata.session_run_index, 0)
    self.assertGreaterEqual(dump.core_metadata.executor_step_index, 0)
    self.assertEqual([ph.name], dump.core_metadata.input_names)
    self.assertEqual([y.name], dump.core_metadata.output_names)
    self.assertEqual([], dump.core_metadata.target_nodes)

    # Despite the fact that the run() call errored out and partition_graphs
    # are not available via run_metadata, the partition graphs should still
    # have been loaded from the dump directory.
    self.assertTrue(dump.loaded_partition_graphs())

    m_dumps = dump.watch_key_to_data("mismatch/m:0:DebugIdentity")
    self.assertEqual(1, len(m_dumps))
    self.assertAllClose(np.array([[1.0, 2.0]]), m_dumps[0].get_tensor())

    x_dumps = dump.watch_key_to_data("mismatch/x:0:DebugIdentity")
    self.assertEqual(1, len(x_dumps))
    self.assertAllClose(np.array([[-3.0, 0.0]]), x_dumps[0].get_tensor())
