# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dense_layer_test.py
"""Tests that the dense layer node is properly compiled in jit scope.
    """

with self.session() as sess:
    x = array_ops.placeholder(shape=[None, None, 3], dtype=np.float32)
    with jit_scope():
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
