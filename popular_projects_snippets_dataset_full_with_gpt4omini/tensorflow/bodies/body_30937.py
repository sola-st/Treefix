# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
collapsed, new_seq_lengths = ctc_ops.collapse_repeated(
    labels=[[1, 3, 3, 3, 0, 0, 0],
            [1, 4, 4, 4, 0, 1, 2],
            [4, 2, 2, 9, 4, 0, 0]],
    seq_length=[4, 5, 5])
self.assertAllEqual(new_seq_lengths, [2, 3, 4])
self.assertAllEqual(
    collapsed,
    [[1, 3, 0, 0],
     [1, 4, 0, 0],
     [4, 2, 9, 4]])
