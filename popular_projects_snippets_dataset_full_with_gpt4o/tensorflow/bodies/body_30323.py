# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
# Batch size mismatched between input and seq_lengths.
# seq_length too long
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            (r"Dimensions must be equal|"
                             r"Length of seq_lengths != input.dims\(0\)")):
    array_ops.reverse_sequence([[1, 2], [3, 4]], [2, 2, 2], seq_axis=1)

# seq_length too short
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            (r"Dimensions must be equal|"
                             r"Length of seq_lengths != input.dims\(0\)")):
    array_ops.reverse_sequence([[1, 2], [3, 4]], [2], seq_axis=1)

# Invalid seq_length shape
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            ("Shape must be rank 1 but is rank 2|"
                             "seq_lengths must be 1-dim")):
    array_ops.reverse_sequence([[1, 2], [3, 4]], [[2, 2]], seq_axis=1)

# seq_axis out of bounds.
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "seq_dim must be < input rank"):
    array_ops.reverse_sequence([[1, 2], [3, 4]], [2, 2], seq_axis=2)

# batch_axis out of bounds.
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "batch_dim must be < input rank"):
    array_ops.reverse_sequence([[1, 2], [3, 4]], [2, 2],
                               seq_axis=1,
                               batch_axis=3)

with self.assertRaisesRegex((errors.OpError, errors.InvalidArgumentError),
                            "batch_dim == seq_dim == 0"):
    output = array_ops.reverse_sequence([[1, 2], [3, 4]], [2, 2], seq_axis=0)
    self.evaluate(output)
