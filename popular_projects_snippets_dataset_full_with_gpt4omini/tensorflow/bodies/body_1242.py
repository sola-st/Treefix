# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_sequence_op_test.py
x = np.asarray(
    [[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]],
     [[17, 18, 19, 20], [21, 22, 23, 24]]],
    dtype=dtype)
x = x.reshape(3, 2, 4, 1, 1)
x = x.transpose([2, 1, 0, 3, 4])  # permute axes 0 <=> 2

# reverse dim 2 up to (0:3, none, 0:4) along dim=0
seq_lengths = np.asarray([3, 0, 4], dtype=len_dtype)

truth_orig = np.asarray(
    [
        [[3, 2, 1, 4], [7, 6, 5, 8]],  # reverse 0:3
        [[9, 10, 11, 12], [13, 14, 15, 16]],  # reverse none
        [[20, 19, 18, 17], [24, 23, 22, 21]]
    ],  # reverse 0:4 (all)
    dtype=dtype)
truth_orig = truth_orig.reshape(3, 2, 4, 1, 1)
truth = truth_orig.transpose([2, 1, 0, 3, 4])  # permute axes 0 <=> 2

seq_axis = 0  # permute seq_axis and batch_axis (originally 2 and 0, resp.)
batch_axis = 2
self._testReverseSequence(x, batch_axis, seq_axis, seq_lengths, truth)
