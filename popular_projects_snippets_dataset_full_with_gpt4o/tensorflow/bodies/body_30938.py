# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
collapsed, new_seq_lengths = ctc_ops.collapse_repeated(
    labels=[[1, 1, 1, 2, 2],
            [1, 1, 1, 2, 2],
            [1, 1, 1, 2, 2]],
    seq_length=[5, 4, 3])
self.assertAllEqual(new_seq_lengths, [2, 2, 1])
self.assertAllEqual(
    collapsed,
    [[1, 2],
     [1, 2],
     [1, 0]])
