# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
"""Converts an IndexedSlices object `value` to a Tensor.

  NOTE(mrry): This function is potentially expensive.

  Args:
    value: An ops.IndexedSlices object.
    dtype: The dtype of the Tensor to be returned.
    name: Optional name to use for the returned Tensor.
    as_ref: True if a ref is requested.

  Returns:
    A dense Tensor representing the values in the given IndexedSlices.

  Raises:
    ValueError: If the IndexedSlices does not have the same dtype.
  """
_ = as_ref
if dtype and not dtype.is_compatible_with(value.dtype):
    raise ValueError(
        f"Incompatible tensor conversion requested to `dtype` {dtype.name} for "
        f"IndexedSlices ({value}) with dtype {value.dtype.name}")
if value.dense_shape is None:
    raise ValueError(
        "Tensor conversion requested for IndexedSlices for argument `value` "
        f"without dense_shape: {value!s}")
# TODO(mrry): Consider adding static shape information to
# IndexedSlices, to avoid using numpy here.
if not context.executing_eagerly():
    dense_shape_value = tensor_util.constant_value(value.dense_shape)
    if dense_shape_value is not None:
        num_elements = np.prod(dense_shape_value)
        if num_elements >= _LARGE_SPARSE_NUM_ELEMENTS:
            warnings.warn(
                "Converting sparse IndexedSlices to a dense Tensor with %d "
                "elements. This may consume a large amount of memory." %
                num_elements)
exit(math_ops.unsorted_segment_sum(
    value.values, value.indices, value.dense_shape[0], name=name))
