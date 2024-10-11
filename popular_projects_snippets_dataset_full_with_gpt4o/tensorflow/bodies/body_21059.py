# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
"""Test that RunOptions from caller and hooks can be merged properly."""

with ops.Graph().as_default():
    my_const = constant_op.constant(42, name='my_const')
    _ = constant_op.constant(24, name='my_const_2')

    hook_watch = debug_pb2.DebugTensorWatch(
        node_name='my_const_2',
        output_slot=0,
        debug_ops=['DebugIdentity'],
        debug_urls=[])
    hook = RunOptionsMetadataHook(2, 60000, False, hook_watch, False)
    with monitored_session.MonitoredSession(hooks=[hook]) as session:
        caller_watch = debug_pb2.DebugTensorWatch(
            node_name='my_const',
            output_slot=0,
            debug_ops=['DebugIdentity'],
            debug_urls=[])
        caller_options = config_pb2.RunOptions(
            trace_level=3,
            timeout_in_ms=30000,
            output_partition_graphs=True,
            report_tensor_allocations_upon_oom=True)
        caller_options.debug_options.debug_tensor_watch_opts.extend(
            [caller_watch])
        self.assertEqual(42, session.run(my_const, options=caller_options))

        # trace_level=3 from the caller should override 2 from the hook.
        # timeout_in_ms=60000 from the hook should override from the caller.
        # output_partition_graph=True from the caller should override False
        # from the hook.
        # The two debug watches from the caller and the hook should be merged,
        # in that order.
        self.assertEqual([
            config_pb2.RunOptions(
                trace_level=3,
                timeout_in_ms=60000,
                output_partition_graphs=True,
                debug_options=debug_pb2.DebugOptions(
                    debug_tensor_watch_opts=[caller_watch, hook_watch]),
                report_tensor_allocations_upon_oom=True),
        ], hook.run_options_list)
        self.assertEqual(1, len(hook.run_metadata_list))
        self.assertTrue(
            isinstance(hook.run_metadata_list[0], config_pb2.RunMetadata))
        self.assertGreater(len(hook.run_metadata_list[0].partition_graphs), 0)
