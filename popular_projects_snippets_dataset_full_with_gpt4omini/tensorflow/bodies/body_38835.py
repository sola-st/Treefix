# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
with self.cached_session():
    for logits_dtype in [np.float16, np.float32, np.float64, \
          dtypes.bfloat16.as_numpy_dtype]:
        for labels_dtype in [np.int32, np.int64]:
            for trial in range(5):
                seed = 123 + trial
                labels, logits = self._generateInputs(
                    labels_dtype, logits_dtype, seed=seed)
                result_a = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
                    labels=labels, logits=logits)
                result_b = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
                    labels=labels, logits=logits)
                self.assertAllEqual(result_a, result_b)
