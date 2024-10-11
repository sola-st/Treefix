# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Replace `SparseTensor`s with their values in `value`

  Each `SparseTensor` in `value` is replaced by its `values` tensor, and
  collects all `SparseTensor`s in `sparse_list`.

  Args:
    value: A structure of `Tensor`s and `SparseTensor`s
    sparse_list: A list. Output parameter that collects all `SparseTensor`s in
      `value`.

  Returns:
    `value` with each SparseTensor replaced by its `.value` attribute.
  """
flat_vals = nest.flatten(value, expand_composites=False)
new_vals = []
for v in flat_vals:
    if isinstance(v, sparse_tensor.SparseTensor):
        sparse_list.append(v)
        new_vals.append(v.values)
    else:
        new_vals.append(v)
exit(nest.pack_sequence_as(value, new_vals, expand_composites=False))
