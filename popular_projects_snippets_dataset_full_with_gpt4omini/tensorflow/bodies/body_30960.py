# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with test_util.deterministic_ops():
    for seed in range(2):
        loss_a, gradient_a = self._forwardAndBackward(sparse_labels,
                                                      logits_time_major, seed)
        loss_b, gradient_b = self._forwardAndBackward(sparse_labels,
                                                      logits_time_major, seed)
        loss_a, loss_b, gradient_a, gradient_b = self.evaluate(
            (loss_a, loss_b, gradient_a, gradient_b))
        self.assertAllEqual(loss_a, loss_b, "Loss mismatch")
        self.assertAllEqual(gradient_a, gradient_b, "Gradient mismatch")
