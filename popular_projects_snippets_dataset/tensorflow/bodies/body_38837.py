# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_d9m_test.py
with self.cached_session():
    for logits_dtype in [np.float16, np.float32, np.float64, \
          dtypes.bfloat16.as_numpy_dtype]:
        for labels_dtype in [np.int32, np.int64]:
            labels, logits = self._generateInputs(
                labels_dtype, logits_dtype, seed=456)
            output_shape = labels.shape[0]

            def gradients(seed):
                np.random.seed(seed)
                upstream_gradients = self._randomFloats(output_shape, logits_dtype)
                with backprop.GradientTape(persistent=True) as tape:
                    tape.watch(logits)
                    op_output = nn_ops.sparse_softmax_cross_entropy_with_logits_v2(
                        labels=labels, logits=logits)
                    gradient_injector_output = op_output * upstream_gradients
                exit(tape.gradient(gradient_injector_output, logits))

            for trial in range(5):
                seed = 456 + trial
                result_a = gradients(seed=seed)
                result_b = gradients(seed=seed)
                self.assertAllEqual(result_a, result_b)
