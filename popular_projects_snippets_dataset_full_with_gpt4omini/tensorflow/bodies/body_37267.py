# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if test_util.is_gpu_available():
    self.skipTest("b/128646478 fails in opensource")

with self.session() as sess:
    with ops.device(test.gpu_device_name()):
        value = constant_op.constant(1.0)
    with ops.device("/cpu:0"):
        true = constant_op.constant(True)
        guarded_assert = control_flow_ops.Assert(true, [value], name="guarded")
        unguarded_assert = gen_logging_ops._assert(
            true, [value], name="unguarded")
    opts = config_pb2.RunOptions(trace_level=config_pb2.RunOptions.FULL_TRACE)
    guarded_metadata = config_pb2.RunMetadata()
    sess.run(guarded_assert, options=opts, run_metadata=guarded_metadata)
    unguarded_metadata = config_pb2.RunMetadata()
    sess.run(unguarded_assert, options=opts, run_metadata=unguarded_metadata)
    guarded_nodestat_names = [
        n.node_name
        for d in guarded_metadata.step_stats.dev_stats
        for n in d.node_stats
    ]
    unguarded_nodestat_names = [
        n.node_name
        for d in unguarded_metadata.step_stats.dev_stats
        for n in d.node_stats
    ]
    guarded_memcpy_nodestat_names = [
        n for n in guarded_nodestat_names if "MEMCPYDtoH" in n
    ]
    unguarded_memcpy_nodestat_names = [
        n for n in unguarded_nodestat_names if "MEMCPYDtoH" in n
    ]
    if "GPU" in [d.device_type for d in device_lib.list_local_devices()]:
        # A copy was performed for the unguarded assert
        self.assertLess(0, len(unguarded_memcpy_nodestat_names),
                        str(unguarded_nodestat_names))
    # No copy was performed for the guarded assert
    self.assertEqual([], guarded_memcpy_nodestat_names)
