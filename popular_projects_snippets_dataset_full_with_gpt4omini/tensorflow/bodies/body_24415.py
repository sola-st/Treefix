# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
"""Test repeated Session.run() calls with debugger increments counters."""

with session.Session() as sess:
    ph = array_ops.placeholder(dtypes.float32, name="successive/ph")
    x = array_ops.transpose(ph, name="mismatch/x")
    y = array_ops.squeeze(ph, name="mismatch/y")

    _, dump1 = self._debug_run_and_get_dump(
        sess, x, feed_dict={ph: np.array([[7.0, 8.0]])}, global_step=1)
    self.assertEqual(1, dump1.core_metadata.global_step)
    self.assertGreaterEqual(dump1.core_metadata.session_run_index, 0)
    self.assertEqual(0, dump1.core_metadata.executor_step_index)
    self.assertEqual([ph.name], dump1.core_metadata.input_names)
    self.assertEqual([x.name], dump1.core_metadata.output_names)
    self.assertEqual([], dump1.core_metadata.target_nodes)
    file_io.delete_recursively(self._dump_root)

    # Calling run() with the same feed, same output and same debug watch
    # options should increment both session_run_index and
    # executor_step_index.
    _, dump2 = self._debug_run_and_get_dump(
        sess, x, feed_dict={ph: np.array([[7.0, 8.0]])}, global_step=2)
    self.assertEqual(2, dump2.core_metadata.global_step)
    self.assertEqual(dump1.core_metadata.session_run_index + 1,
                     dump2.core_metadata.session_run_index)
    self.assertEqual(dump1.core_metadata.executor_step_index + 1,
                     dump2.core_metadata.executor_step_index)
    self.assertEqual([ph.name], dump2.core_metadata.input_names)
    self.assertEqual([x.name], dump2.core_metadata.output_names)
    self.assertEqual([], dump2.core_metadata.target_nodes)
    file_io.delete_recursively(self._dump_root)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options, sess.graph, debug_urls=self._debug_urls(), global_step=3)

    # Calling run() with a different output should increment
    # session_run_index, but not executor_step_index.
    _, dump3 = self._debug_run_and_get_dump(
        sess, y, feed_dict={ph: np.array([[7.0, 8.0]])}, global_step=3)
    self.assertEqual(3, dump3.core_metadata.global_step)
    self.assertEqual(dump2.core_metadata.session_run_index + 1,
                     dump3.core_metadata.session_run_index)
    self.assertEqual(0, dump3.core_metadata.executor_step_index)
    self.assertEqual([ph.name], dump3.core_metadata.input_names)
    self.assertEqual([y.name], dump3.core_metadata.output_names)
    self.assertEqual([], dump3.core_metadata.target_nodes)
