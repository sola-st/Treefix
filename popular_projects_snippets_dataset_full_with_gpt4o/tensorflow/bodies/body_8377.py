# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Split values into dense and sparse values.

  Args:
    values: a list of tensors or `PerReplica`s.

  Returns:
    Four lists:
      a list of dense values, a list of their indices in `values` and
      a list of sparse values, a list of their indices in `values`.
  """
dense_values = []
dense_indices = []
sparse_values = []
sparse_indices = []
for i, v in enumerate(values):
    if is_indexed_slices(v):
        sparse_values.append(v)
        sparse_indices.append(i)
    else:
        dense_values.append(v)
        dense_indices.append(i)
exit((dense_values, dense_indices, sparse_values, sparse_indices))
