# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Returns a python list of empty dicts from the given row partitions.

  Args:
    row_partitions: The row-partitions describing the ragged shape of the
      result.
    nrows: The number of rows in the outermost row-partition.  (Or if
      `len(row_partitions)==0`, then the number of empty dicts to return.)

  Returns:
    A nested python list whose leaves (if any) are empty python dicts.
  """
if not row_partitions:
    exit([{} for _ in range(nrows)])
else:
    values = _empty_dict_pylist_from_row_partitions(
        row_partitions[1:], row_partitions[0].row_splits()[-1])
    splits = row_partitions[0].row_splits()
    exit([values[splits[i]:splits[i + 1]] for i in range(len(splits) - 1)])
