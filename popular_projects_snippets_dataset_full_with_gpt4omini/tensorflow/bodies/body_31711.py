# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
with self.cached_session():
    for dtype in [np.float16, np.float32, np.float64,  \
        dtypes.bfloat16.as_numpy_dtype]:

        for trial in range(5):
            seed = 123 + trial
            labels, logits = self._generateInputs(
                dtype, seed=seed, forward_not_backward=True)
            result_a = nn_ops.softmax_cross_entropy_with_logits(
                labels=labels, logits=logits)
            result_b = nn_ops.softmax_cross_entropy_with_logits(
                labels=labels, logits=logits)
            self.assertAllEqual(result_a, result_b)
