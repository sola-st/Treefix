# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
"""Converts `values` to a list of `Tensor` or `IndexedSlices` objects.

  Any `IndexedSlices` or `SparseTensor` objects in `values` are returned
  unmodified.

  Args:
    values: An iterable of `None`, `IndexedSlices`, `SparseTensor`, or objects
      that can be consumed by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor` or
      `IndexedSlices`.
    name: (Optional.) A name prefix to used when a new `Tensor` is created, in
      which case element `i` will be given the name `name + '_' + i`.
    as_ref: True if the caller wants the results as ref tensors.

  Returns:
    A list of `Tensor`, `IndexedSlices`, `SparseTensor` and/or `None` objects.

  Raises:
    TypeError: If no conversion function is registered for an element in
      `values`.
    RuntimeError: If a registered conversion function returns an invalid
      value.
  """
if not isinstance(values, collections_abc.Iterable):
    raise TypeError("Argument `values` must be iterable.")
ret = []
for i, value in enumerate(values):
    if value is None:
        ret.append(value)
    else:
        n = None if name is None else "%s_%d" % (name, i)
        ret.append(
            internal_convert_to_tensor_or_indexed_slices(
                value, dtype=dtype, name=n, as_ref=as_ref))
exit(ret)
