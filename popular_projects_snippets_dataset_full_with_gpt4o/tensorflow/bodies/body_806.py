# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dense_layer_test.py
"""Tests dense layer compilation in auto-jit mode.

    Dense layer should be compiled into a single XlaCompile/XlaRun op pair in
    auto-jit mode.
    """

os.environ["TF_XLA_FLAGS"] = (
    "--tf_xla_cpu_global_jit " + os.environ.get("TF_XLA_FLAGS", ""))
config = config_pb2.ConfigProto()
config.graph_options.optimizer_options.global_jit_level = (
    config_pb2.OptimizerOptions.ON_1)

with self.session(config=config) as sess:
    x = array_ops.placeholder(shape=[None, None, 3], dtype=np.float32)
    y = layers.dense(x, 3)

    self.evaluate(variables.global_variables_initializer())
    run_metadata = config_pb2.RunMetadata()
    test_utils.RunWithWarmup(
        sess,
        y, {x: np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])},
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))

labels = GetRunMetadataLabels(run_metadata)
self.assertEqual(1, self.countXlaOps(labels))
self.assertFalse(InLabels(labels, "MatMult"))
