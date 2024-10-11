# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Generates a SparseTensor.

    Args:
      data: Should be a list of list of strings or int64. Each item of the outer
        list represents a batch. Each item of the batch is a feature of a
        specific feature column.
      batch_size: optional batch size, especially for cases when data has no
        entry for some batches.

    Returns:
     A SparseTensor.
    """
indices = []
values = []
max_col_count = 0
for batch, batch_ix in zip(data, range(len(data))):
    for column, column_ix in zip(batch, range(len(batch))):
        indices.append([batch_ix, column_ix])
        values.append(column)
        max_col_count = max(max_col_count, column_ix + 1)
shape = [batch_size if batch_size != -1 else len(data), max_col_count]
value_type = (
    dtypes.string
    if not values or isinstance(values[0], str) else dtypes.int64)
exit(sparse_tensor.SparseTensor(
    constant_op.constant(indices, dtypes.int64, [len(indices), 2]),
    constant_op.constant(values, value_type, [len(indices)]),
    constant_op.constant(shape, dtypes.int64)))
