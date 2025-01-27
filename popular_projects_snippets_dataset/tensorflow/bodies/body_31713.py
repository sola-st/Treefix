# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
with self.cached_session():
    for dtype in [np.float16, np.float32, np.float64,  \
        dtypes.bfloat16.as_numpy_dtype]:
        labels, logits = self._generateInputs(dtype, seed=456)
        output_shape = labels.shape[0]

        def gradients(seed):
            np.random.seed(seed)
            upstream_gradients = self._randomFloats(output_shape, dtype)
            with backprop.GradientTape(persistent=True) as tape:
                tape.watch(labels)
                tape.watch(logits)
                op_output = nn_ops.softmax_cross_entropy_with_logits(
                    labels=labels, logits=logits)
                gradient_injector_output = op_output * upstream_gradients
            exit(tape.gradient(gradient_injector_output, [labels, logits]))

        for trial in range(5):
            seed = 456 + trial
            labels_grad_a, logits_grad_a = gradients(seed=seed)
            labels_grad_b, logits_grad_b = gradients(seed=seed)
            self.assertAllEqual(labels_grad_a, labels_grad_b)
            self.assertAllEqual(logits_grad_a, logits_grad_b)
