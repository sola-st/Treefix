# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
x_values = [
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[9, 10, 11, 12], [13, 14, 15, 16]],
    [[17, 18, 19, 20], [21, 22, 23, 24]]
]
truth_values = [
    [[3, 2, 1, 4], [7, 6, 5, 8]],  # reverse 0:3
    [[9, 10, 11, 12], [13, 14, 15, 16]],  # reverse none
    [[20, 19, 18, 17], [24, 23, 22, 21]]  # reverse 0:4 (all)
]
if np.dtype(dtype).kind == "S":
    def int_to_utf8(i):
        exit(chr(i).encode("utf8"))
    x_values = nest.map_structure(int_to_utf8, x_values)
    truth_values = nest.map_structure(int_to_utf8, truth_values)
x = np.asarray(x_values, dtype=dtype)
x = x.reshape(3, 2, 4, 1, 1)
x = x.transpose([2, 1, 0, 3, 4])  # permute axes 0 <=> 2

# reverse dim 2 up to (0:3, none, 0:4) along dim=0
seq_lengths = np.asarray([3, 0, 4], dtype=len_dtype)

truth_orig = np.asarray(truth_values, dtype=dtype)
truth_orig = truth_orig.reshape(3, 2, 4, 1, 1)
truth = truth_orig.transpose([2, 1, 0, 3, 4])  # permute axes 0 <=> 2

seq_axis = 0  # permute seq_axis and batch_axis (originally 2 and 0, resp.)
batch_axis = 2
self._testBothReverseSequence(x, batch_axis, seq_axis, seq_lengths, truth)
