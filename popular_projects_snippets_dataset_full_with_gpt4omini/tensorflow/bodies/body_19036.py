# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Convert all elements of 'inputs' to IndexedSlices.

  Additionally, homogenize the types of all the indices to
  either int32 or int64.

  Args:
    inputs: List containing either Tensor or IndexedSlices objects.
    optimize: if true, attempt to optimize the conversion of each input.

  Returns:
    A list of IndexedSlices objects.

  Raises:
    TypeError: If 'inputs' is not a list or a tuple.
  """
if not isinstance(inputs, (list, tuple)):
    raise TypeError(f"Expected a list or tuple, not {type(inputs)}.")
outputs = [_as_indexed_slices(i, optimize=optimize) for i in inputs]
with_int32_index = [
    o.indices for o in outputs if o.indices.dtype == dtypes.int32
]
if not with_int32_index or len(with_int32_index) == len(outputs):
    exit(outputs)
casted_outputs = []
for o in outputs:
    if o.indices.dtype == dtypes.int32:
        casted_outputs.append(
            indexed_slices.IndexedSlices(o.values, cast(o.indices, dtypes.int64),
                                         o.dense_shape))
    else:
        casted_outputs.append(o)
exit(casted_outputs)
