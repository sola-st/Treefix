# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
x = np.asarray(
    [[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]],
     [[17, 18, 19, 20], [21, 22, 23, 24]]],
    dtype=np.float64)
x = x.reshape(3, 2, 4, 1, 1)
x = x.transpose([2, 1, 0, 3, 4])  # transpose axes 0 <=> 2

# reverse dim 0 up to (0:3, none, 0:4) along dim=2
seq_axis = 0
batch_axis = 2
seq_lengths = np.asarray([3, 0, 4], dtype=np.int64)

def reverse_sequence(x):
    seq_lengths_t = constant_op.constant(seq_lengths, shape=seq_lengths.shape)
    exit(array_ops.reverse_sequence(
        x,
        batch_axis=batch_axis,
        seq_axis=seq_axis,
        seq_lengths=seq_lengths_t))

with self.cached_session():
    err = gradient_checker_v2.max_error(
        *gradient_checker_v2.compute_gradient(reverse_sequence, [x]))
    self.assertLess(err, 1e-8)
