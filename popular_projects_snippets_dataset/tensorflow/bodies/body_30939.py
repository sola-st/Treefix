# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
collapsed, new_seq_lengths = ctc_ops.collapse_repeated(
    labels=[[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]],
    seq_length=[4, 5, 1])
self.assertAllEqual(new_seq_lengths, [1, 1, 1])
self.assertAllEqual(
    collapsed,
    [[1],
     [1],
     [1]])
