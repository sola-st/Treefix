# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
inputs = np.random.randn(2, 2, 3).astype(np.float32)
inputs_t = constant_op.constant(inputs)
labels = SimpleSparseTensorFrom([[0, 1], [1, 0]])
seq_lens = np.array([2, 2], dtype=np.int32)
v = [1.0]

with self.session(use_gpu=False):
    loss = _ctc_loss_v2(
        inputs=inputs_t, labels=labels, sequence_length=seq_lens)
    # Taking this second gradient should fail, since it is not
    # yet supported.
    with self.assertRaisesRegex(LookupError, "explicitly disabled"):
        _ = gradients_impl._hessian_vector_product(loss, [inputs_t], v)
