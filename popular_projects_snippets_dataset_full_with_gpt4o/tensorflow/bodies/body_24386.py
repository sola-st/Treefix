# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
"""Run fetches with debugging and obtain DebugDumpDir.

    Args:
      sess: the tf.compat.v1.Session to be used.
      fetches: fetches of the Session.run().
      feed_dict: feed dict for the Session.run().
      debug_ops: name(s) of the debug ops to be used.
      tolerate_debug_op_creation_failures: whether to tolerate debug op
        creation failures.
      global_step: Optional global step.
      validate: whether to validate dumped tensors against graph.
      expected_partition_graph_count: optional count of partition graphs to
        assert on.

    Returns:
      1. Return values of the Session.run().
      2. The DebugDumpDir object from the debugged run().
    """

run_options = config_pb2.RunOptions(output_partition_graphs=True)
debug_utils.watch_graph(
    run_options,
    sess.graph,
    debug_ops=debug_ops,
    debug_urls=self._debug_urls(),
    tolerate_debug_op_creation_failures=tolerate_debug_op_creation_failures,
    global_step=global_step)
run_metadata = config_pb2.RunMetadata()
run_output = sess.run(fetches,
                      feed_dict=feed_dict,
                      options=run_options,
                      run_metadata=run_metadata)

if expected_partition_graph_count is not None:
    self.assertEqual(expected_partition_graph_count,
                     len(run_metadata.partition_graphs))
exit((run_output, debug_data.DebugDumpDir(
    self._dump_root, partition_graphs=run_metadata.partition_graphs,
    validate=validate)))
