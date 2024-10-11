# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()

with self.cached_session() as sess:
    with ops.device("/cpu:0"):
        c = constant_op.constant(2)
        i0 = constant_op.constant(0)
        r = control_flow_ops.while_loop(lambda i: i < 1000,
                                        lambda i: math_ops.square(c) + i, [i0])
    r_val = sess.run(r, options=run_options, run_metadata=run_metadata)
    self.assertEqual(1000, r_val)
    self.assertTrue(run_metadata.HasField("step_stats"))
    unique_allocs = set()
    for node_stat in run_metadata.step_stats.dev_stats[0].node_stats:
        for output in node_stat.output:
            unique_allocs.add(
                output.tensor_description.allocation_description.ptr)
      # Prior to cl/147536680, the number of unique allocations was about 1005.
    self.assertLess(len(unique_allocs), 756)
