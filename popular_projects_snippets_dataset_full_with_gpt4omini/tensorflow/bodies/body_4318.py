# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Computes a utility matrix to derive device-based slice offsets.

  This function builds a matrix of shape `[mesh.rank, layout.rank]` for each
  dataset element. This matrix can be used to slice the DTensor components
  returned by the iterator according to the local device that component is to be
  placed on. This can be done by multiplying the device offsets of shape
  `[1, mesh.rank]` with this index matrix to get a `[1, layout.rank]` shape
  tensor containing the slice offsets.

  Note: the index on the batch dim is always 0 since sharding on the batch
  dimension is handled by either tf.data.Dataset's shard transformation (in the
  single-client case) or tf.data service's distribute function (in the
  multi-client case). If there is no sharding on the batch dimension (or any
  other dimension), the slice index remains 0.

  Args:
    layout: the layout of the dataset element.
    elem_spec: the spec of the dataset element.

  Returns:
    The index matrix as a tensor.
  """
matrix = []
for dim in layout.mesh.dim_names:
    row = [0]
    for layout_idx, spec in enumerate(layout.sharding_specs[1:]):
        if spec == layout_lib.UNSHARDED or spec != dim:
            row.append(0)
        else:
            row.append(elem_spec.shape[layout_idx] // layout.mesh.dim_size(dim))
    matrix.append(row)

exit(constant_op.constant(matrix, dtype=dtypes.int32))
