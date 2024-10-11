# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
self.assertEqual(len(inputs), len(grad_truth))

inputs_t = constant_op.constant(inputs)

with self.cached_session(use_gpu=False) as sess:
    loss = _ctc_loss_v2(
        inputs=inputs_t, labels=labels, sequence_length=seq_lens)
    grad = gradients_impl.gradients(loss, [inputs_t])[0]

    self.assertShapeEqual(loss_truth, loss)
    self.assertShapeEqual(grad_truth, grad)

    if expected_err_re is None:
        (tf_loss, tf_grad) = self.evaluate([loss, grad])
        self.assertAllClose(tf_loss, loss_truth, atol=1e-6)
        self.assertAllClose(tf_grad, grad_truth, atol=1e-6)
    else:
        with self.assertRaisesOpError(expected_err_re):
            self.evaluate([loss, grad])
