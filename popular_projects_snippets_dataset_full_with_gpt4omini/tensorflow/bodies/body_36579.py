# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
old = control_flow_util_v2._DISABLE_LOWER_USING_SWITCH_MERGE
control_flow_util_v2._DISABLE_LOWER_USING_SWITCH_MERGE = True
with self.session() as sess:
    x = constant_op.constant(2.)
    ret = while_loop_v2(
        lambda v: v < 8., lambda v: v * v, [x], return_same_structure=False)

    opts = config_pb2.RunOptions(trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata = config_pb2.RunMetadata()
    self.assertEqual(sess.run(ret, options=opts, run_metadata=run_metadata),
                     16)
    for dev_stat in run_metadata.step_stats.dev_stats:
        for ns in dev_stat.node_stats:
            self.assertNotIn("switch", ns.node_name)
control_flow_util_v2._DISABLE_LOWER_USING_SWITCH_MERGE = old
