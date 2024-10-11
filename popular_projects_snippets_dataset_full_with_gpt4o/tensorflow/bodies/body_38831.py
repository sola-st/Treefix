# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
with self.session(), test_util.force_gpu():
    for features_dtype in [dtypes.float16, dtypes.float32]:
        for labels_dtype in [dtypes.int32, dtypes.int64]:
            features = constant_op.constant([[0.3, 0.5], [0.2, 0.6]],
                                            dtype=features_dtype)
            labels = constant_op.constant([1, 0], dtype=labels_dtype)
            with self.assertRaisesRegex(
                errors_impl.UnimplementedError,
                "The GPU implementation of SparseSoftmaxCrossEntropyWithLogits " +
                "that would have been executed is not deterministic. Note that " +
                "the Python API uses an alternative, deterministic, " +
                "GPU-accelerated path when determinsim is enabled."):
                result = gen_nn_ops.sparse_softmax_cross_entropy_with_logits(
                    features=features, labels=labels)
                self.evaluate(result)
