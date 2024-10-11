# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
seq_lengths_t = constant_op.constant(seq_lengths, shape=seq_lengths.shape)
exit(array_ops.reverse_sequence(
    x,
    batch_axis=batch_axis,
    seq_axis=seq_axis,
    seq_lengths=seq_lengths_t))
