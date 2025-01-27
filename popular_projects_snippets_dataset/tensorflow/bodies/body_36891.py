# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if test_util.is_gpu_available():
    self.skipTest(
        "Single threaded executor doesn't support partitioned graphs.  "
        "Skipping GPU test.")
# Make pred feedable to ensure we don't constant-fold it out.
run_opts = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata_no_lowering = config_pb2.RunMetadata()
run_metadata_with_lowering = config_pb2.RunMetadata()

config = opt_cfg(do_constant_folding=False)

pred = array_ops.placeholder_with_default(
    constant_op.constant(True), shape=())
r = control_flow_ops.cond(pred, lambda: True, lambda: False)

with session.Session(config=config) as sess:
    r_value = sess.run(
        r, options=run_opts, run_metadata=run_metadata_with_lowering)
    self.assertEqual(r_value, True)

# Use the single threaded executor, which disables control flow lowering.
config.experimental.executor_type = "SINGLE_THREADED_EXECUTOR"
with session.Session(config=config) as sess:
    r_value = sess.run(
        r, options=run_opts, run_metadata=run_metadata_no_lowering)
    self.assertEqual(r_value, True)

self.assertTrue(  # pylint: disable=g-complex-comprehension
    any("switch" in ns.node_name
        for dev_stat in run_metadata_with_lowering.step_stats.dev_stats
        for ns in dev_stat.node_stats))

self.assertTrue(  # pylint: disable=g-complex-comprehension
    all("switch" not in ns.node_name
        for dev_stat in run_metadata_no_lowering.step_stats.dev_stats
        for ns in dev_stat.node_stats))
