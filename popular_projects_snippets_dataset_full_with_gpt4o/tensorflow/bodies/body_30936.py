# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
collapsed, new_seq_lengths = ctc_ops.collapse_repeated(
    labels=constant_op.constant(
        [[1, 3, 3, 3, 0],
         [1, 4, 4, 4, 0],
         [4, 2, 2, 9, 4]],
        dtype=dtypes.int64),
    seq_length=constant_op.constant([4, 5, 5], dtype=dtypes.int64))
self.assertEqual(new_seq_lengths.dtype, dtypes.int64)
self.assertEqual(collapsed.dtype, dtypes.int64)
self.assertAllEqual(new_seq_lengths, [2, 3, 4])
self.assertAllEqual(
    collapsed,
    [[1, 3, 0, 0],
     [1, 4, 0, 0],
     [4, 2, 9, 4]])
