# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
"""Test for rewriting RunOptions and observing RunMetadata with hooks."""

with ops.Graph().as_default():
    my_const = constant_op.constant(42, name='my_const')
    _ = constant_op.constant(24, name='my_const_2')

    watch_a = debug_pb2.DebugTensorWatch(
        node_name='my_const',
        output_slot=0,
        debug_ops=['DebugIdentity'],
        debug_urls=[])
    hook_a = RunOptionsMetadataHook(2, 30000, False, watch_a, False)
    watch_b = debug_pb2.DebugTensorWatch(
        node_name='my_const_2',
        output_slot=0,
        debug_ops=['DebugIdentity'],
        debug_urls=[])
    hook_b = RunOptionsMetadataHook(3, 60000, True, watch_b, True)
    with monitored_session.MonitoredSession(
        hooks=[hook_a, hook_b]) as session:
        self.assertEqual(42, session.run(my_const))

        # trace_level=3 should have overridden trace_level=2;
        # timeout_in_ms=60000 should have overridden 30000;
        # output_partition_graphs=True should have overridden False.
        # The two debug tensor watches should have been merged.
        self.assertEqual([
            config_pb2.RunOptions(
                trace_level=3,
                timeout_in_ms=60000,
                output_partition_graphs=True,
                debug_options=debug_pb2.DebugOptions(
                    debug_tensor_watch_opts=[watch_a, watch_b]),
                report_tensor_allocations_upon_oom=True),
        ], hook_b.run_options_list)
        self.assertEqual(1, len(hook_b.run_metadata_list))
        self.assertTrue(
            isinstance(hook_b.run_metadata_list[0], config_pb2.RunMetadata))
        self.assertGreater(len(hook_b.run_metadata_list[0].partition_graphs), 0)
