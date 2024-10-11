# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
if context.executing_eagerly():
    exit()
with self.cached_session():
    self.assertAllClose(*self.evaluate([loss, ref_loss]))
    grad = gradients_impl.gradients(loss, [logits])
    self.assertAllClose(
        *self.evaluate([grad, ref_grad]), rtol=2e-06, atol=2e-06)
