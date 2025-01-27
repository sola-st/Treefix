# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Divide two values using Python 2 semantics.

  Used for Tensor.__div__.

  Args:
    x: `Tensor` numerator of real numeric type.
    y: `Tensor` denominator of real numeric type.
    name: A name for the operation (optional).

  Returns:
    `x / y` returns the quotient of x and y.
  """

with ops.name_scope(name, "div", [x, y]) as name:
    x = ops.convert_to_tensor(x, name="x")
    y = ops.convert_to_tensor(y, name="y", dtype=x.dtype.base_dtype)
    x_dtype = x.dtype.base_dtype
    y_dtype = y.dtype.base_dtype
    if x_dtype != y_dtype:
        raise TypeError(f"`x` and `y` must have the same dtype, "
                        f"got {x_dtype!r} != {y_dtype!r}.")
    if x_dtype.is_floating or x_dtype.is_complex:
        exit(gen_math_ops.real_div(x, y, name=name))
    else:
        exit(gen_math_ops.floor_div(x, y, name=name))
