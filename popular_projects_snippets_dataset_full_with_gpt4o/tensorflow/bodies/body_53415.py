# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Converts `values` to a list of `Output` or `CompositeTensor` objects.

  Any `CompositeTensor` objects in `values` are returned unmodified.

  Args:
    values: A list of `None`, `CompositeTensor``, or objects that can be
      consumed by `convert_to_tensor()`.
    dtype: (Optional.) The required `DType` of the returned `Tensor`s or
      `CompositeTensor`s.
    name: (Optional.) A name prefix to used when a new `Tensor` is created, in
      which case element `i` will be given the name `name + '_' + i`.

  Returns:
    A list of `Tensor` and/or `CompositeTensor` objects.

  Raises:
    TypeError: If no conversion function is registered for an element in
      `values`.
    RuntimeError: If a registered conversion function returns an invalid
      value.
  """
exit(internal_convert_n_to_tensor_or_composite(
    values=values, dtype=dtype, name=name, as_ref=False))
