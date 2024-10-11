# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
"""Verifies the output values of the glimpse extraction kernel.

    Args:
      tensor_in_sizes: Input tensor dimensions in [input_rows, input_cols].
      glimpse_sizes: Dimensions of the glimpse in [glimpse_rows, glimpse_cols].
      offsets: Relative location of the center of the glimpse in the input
        image expressed as [row_offset, col_offset].
      expected_rows: A list containing the expected row numbers (None for
         out of bound entries that are expected to be replaced by uniform
         random entries in [0,1) ).
      expected_cols: Same as expected_rows, but for column numbers.
    """

rows = tensor_in_sizes[0]
cols = tensor_in_sizes[1]
# Row Tensor with entries by row.
# [[ 1 1 1 ... ]
#  [ 2 2 2 ... ]
#  [ 3 3 3 ... ]
#  [ ...
# ]
t_rows = array_ops.tile(
    [[1.0 * r] for r in range(1, rows + 1)], [1, cols], name='tile_rows')

# Shuffle to switch to a convention of (batch_size, height, width, depth).
t_rows_4d = array_ops.transpose(
    array_ops.expand_dims(array_ops.expand_dims(t_rows, 0), 3),
    [0, 2, 1, 3])

# Column Tensor with entries by column.
# [[ 1 2 3 4 ... ]
#  [ 1 2 3 4 ... ]
#  [ 1 2 3 4 ... ]
#  [ ...         ]
# ]
t_cols = array_ops.tile(
    [[1.0 * r for r in range(1, cols + 1)]], [rows, 1], name='tile_cols')

# Shuffle to switch to a convention of (batch_size, height, width, depth).
t_cols_4d = array_ops.transpose(
    array_ops.expand_dims(array_ops.expand_dims(t_cols, 0), 3),
    [0, 2, 1, 3])

# extract_glimpses from Row and Column Tensor, respectively.
# Switch order for glimpse_sizes and offsets to switch from (row, col)
# convention to tensorflows (height, width) convention.
t1 = constant_op.constant([glimpse_sizes[1], glimpse_sizes[0]], shape=[2])
t2 = constant_op.constant([offsets[1], offsets[0]], shape=[1, 2])
glimpse_rows = (array_ops.transpose(
    image_ops.extract_glimpse(t_rows_4d, t1, t2), [0, 2, 1, 3]))
glimpse_cols = (array_ops.transpose(
    image_ops.extract_glimpse(t_cols_4d, t1, t2), [0, 2, 1, 3]))

# Evaluate the TensorFlow Graph.
with self.cached_session() as sess:
    value_rows, value_cols = self.evaluate([glimpse_rows, glimpse_cols])

# Check dimensions of returned glimpse.
self.assertEqual(value_rows.shape[1], glimpse_sizes[0])
self.assertEqual(value_rows.shape[2], glimpse_sizes[1])
self.assertEqual(value_cols.shape[1], glimpse_sizes[0])
self.assertEqual(value_cols.shape[2], glimpse_sizes[1])

# Check entries.
min_random_val = 0
max_random_val = max(rows, cols)
for i in range(glimpse_sizes[0]):
    for j in range(glimpse_sizes[1]):
        if expected_rows[i] is None or expected_cols[j] is None:
            self.assertGreaterEqual(value_rows[0][i][j][0], min_random_val)
            self.assertLessEqual(value_rows[0][i][j][0], max_random_val)
            self.assertGreaterEqual(value_cols[0][i][j][0], min_random_val)
            self.assertLessEqual(value_cols[0][i][j][0], max_random_val)
        else:
            self.assertEqual(value_rows[0][i][j][0], expected_rows[i])
            self.assertEqual(value_cols[0][i][j][0], expected_cols[j])
