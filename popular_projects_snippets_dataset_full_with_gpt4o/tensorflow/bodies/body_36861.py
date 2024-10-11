# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = array_ops.placeholder(dtypes.float32)

# `arg` is used in the cond then branch so a Switch node is created for it.
# We test that the Switch node gets placed on the same device as `arg`.
# We force `arg` to be on CPU here.
with ops.device("CPU:0"):
    arg = x + 10.

def true_fn():
    with ops.device("CPU:0"):
        exit(arg + 1)

r = control_flow_ops.cond(constant_op.constant(True), true_fn, lambda: 0.)

# Disable Loop_optimizer grappler pass for this test because it replaces
# Switch with Identity when it's part of a dead branch.
config = config_pb2.ConfigProto()
config.graph_options.rewrite_options.loop_optimization = (
    rewriter_config_pb2.RewriterConfig.OFF)

with self.session(config=config) as sess:
    run_metadata = config_pb2.RunMetadata()
    options = config_pb2.RunOptions(output_partition_graphs=True)
    sess.run(
        r, feed_dict={x: -10.}, options=options, run_metadata=run_metadata)
    self.assertLen(run_metadata.partition_graphs, 2)
    # Check that the Switch for `arg` gets placed on CPU.
    self.assertEqual(
        self._count_matching_switch_nodes_on_device(run_metadata, "CPU",
                                                    dtypes.float32), 1)
    self.assertEqual(
        self._count_matching_switch_nodes_on_device(run_metadata, "GPU",
                                                    dtypes.float32), 0)
