# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
with self.session(), test_util.force_gpu():
    for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
        features = constant_op.constant([[0.3, 0.5], [0.5, 0.6]], dtype=dtype)
        labels = constant_op.constant([[0.2, 0.4], [0.1, 0.2]], dtype=dtype)
        with self.assertRaisesRegex(
            errors_impl.UnimplementedError,
            "The GPU implementation of SoftmaxCrossEntropyWithLogits that " +
            "would have been executed is not deterministic. Note that the " +
            "Python API uses an alternative, deterministic, GPU-accelerated " +
            "path when determinism is enabled."):
            result = gen_nn_ops.softmax_cross_entropy_with_logits(
                features=features, labels=labels)
            self.evaluate(result)
