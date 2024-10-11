# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
np.random.seed(seed)
params = self._genInputParams(
    logits_time_major=logits_time_major, sparse_labels=sparse_labels)
labels, logits, labels_lengths, logits_lengths = params
output_shape = (labels_lengths.shape[0],)
upstream_gradients = self._randomFloats(output_shape)
with backprop.GradientTape() as tape:
    tape.watch(logits)
    loss = ctc_ops.ctc_loss_v3(
        labels,
        logits,
        labels_lengths,
        logits_lengths,
        logits_time_major=logits_time_major,
        blank_index=0)
    gradient_injector_output = loss * upstream_gradients
exit((loss, tape.gradient(gradient_injector_output, logits)))
