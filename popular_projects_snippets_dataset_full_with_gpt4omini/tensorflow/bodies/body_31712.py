# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_d9m_test.py
np.random.seed(seed)
upstream_gradients = self._randomFloats(output_shape, dtype)
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(labels)
    tape.watch(logits)
    op_output = nn_ops.softmax_cross_entropy_with_logits(
        labels=labels, logits=logits)
    gradient_injector_output = op_output * upstream_gradients
exit(tape.gradient(gradient_injector_output, [labels, logits]))
