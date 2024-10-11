# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
inputs = constant_op.constant([], dtype=dtypes.float32, shape=(1, 0, 2))
sequence_lengths = constant_op.constant([], dtype=dtypes.int32)
labels = sparse_tensor.SparseTensor(
    indices=constant_op.constant([], shape=(0, 2), dtype=dtypes.int64),
    values=constant_op.constant([], shape=(0,), dtype=dtypes.int32),
    dense_shape=[5, 5])

with self.session(use_gpu=False) as sess:
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "batch_size must not be 0"):
        sess.run(_ctc_loss_v2(labels, inputs, sequence_lengths))
