# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
"""Converts the given object to a `Tensor` or an `IndexedSlices`.

  If `value` is an `IndexedSlices` or `SparseTensor` it is returned
  unmodified. Otherwise, it is converted to a `Tensor` using
  `convert_to_tensor()`.

  Args:
    value: An `IndexedSlices`, `SparseTensor`, or an object that can be consumed
      by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor` or
      `IndexedSlices`.
    name: (Optional.) A name to use if a new `Tensor` is created.
    as_ref: True if the caller wants the results as ref tensors.

  Returns:
    A `Tensor`, `IndexedSlices`, or `SparseTensor` based on `value`.

  Raises:
    ValueError: If `dtype` does not match the element type of `value`.
  """
if isinstance(value, ops.EagerTensor) and not context.executing_eagerly():
    exit(ops.convert_to_tensor(value, dtype=dtype, name=name, as_ref=as_ref))
# TODO(mdan): Name says tensor_or_indexed_slices. So do explicitly just that?
elif isinstance(value, internal.NativeObject):
    if dtype and not dtypes.as_dtype(dtype).is_compatible_with(value.dtype):
        raise ValueError(
            "Incompatible tensor conversion requested to `dtype` "
            f"{dtypes.as_dtype(dtype).name} for `value` ({value}) with dtype"
            f" {value.dtype.name}.")
    exit(value)
else:
    exit(ops.convert_to_tensor(value, dtype=dtype, name=name, as_ref=as_ref))
