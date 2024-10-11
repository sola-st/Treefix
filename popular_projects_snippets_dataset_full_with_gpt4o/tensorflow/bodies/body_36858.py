# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant(-10.)

# True branch function defined outside of device scope
def true_fn():
    exit(math_ops.exp(x))

with ops.device("CPU:0"):
    r = control_flow_ops.cond(
        constant_op.constant(True), true_fn, lambda: 0.)
    self.assertIn("cpu", r.device.lower())

with session.Session() as sess:
    options = config_pb2.RunOptions(output_partition_graphs=True)
    run_metadata = config_pb2.RunMetadata()
    sess.run(r, options=options, run_metadata=run_metadata)
    # We expect that everything runs on CPU, even if GPU is available.
    self.assertEqual(len(run_metadata.partition_graphs), 1)
