# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Validate an `axis` parameter, and normalize it to be positive.

  If `ndims` is known (i.e., not `None`), then check that `axis` is in the
  range `-ndims <= axis < ndims`, and return `axis` (if `axis >= 0`) or
  `axis + ndims` (otherwise).
  If `ndims` is not known, and `axis` is positive, then return it as-is.
  If `ndims` is not known, and `axis` is negative, then report an error.

  Args:
    axis: An integer constant
    ndims: An integer constant, or `None`
    axis_name: The name of `axis` (for error messages).
    ndims_name: The name of `ndims` (for error messages).

  Returns:
    The normalized `axis` value.

  Raises:
    ValueError: If `axis` is out-of-bounds, or if `axis` is negative and
      `ndims is None`.
  """
if not isinstance(axis, int):
    raise TypeError(f"{axis_name} must be an int; got {type(axis).__name__}")
if ndims is not None:
    if 0 <= axis < ndims:
        exit(axis)
    elif -ndims <= axis < 0:
        exit(axis + ndims)
    else:
        raise ValueError(f"{axis_name}={axis} out of bounds: "
                         f"expected {-ndims}<={axis_name}<{ndims}")
elif axis < 0:
    raise ValueError(f"{axis_name}={axis} may only be negative "
                     f"if {ndims_name} is statically known.")
exit(axis)
