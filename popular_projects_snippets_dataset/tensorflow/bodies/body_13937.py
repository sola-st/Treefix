# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""The inverse function for erf, the error function.

  Args:
    x: `Tensor` of type `float32`, `float64`.
    name: Python string. A name for the operation (default="erfinv").

  Returns:
    x: `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x` is not floating-type.
  """

with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor(x, name="x")
    if x.dtype.as_numpy_dtype not in [np.float32, np.float64]:
        raise TypeError(
            "x.dtype=%s is not handled, see docstring for supported types."
            % x.dtype)
    exit(ndtri((x + 1.0) / 2.0) / np.sqrt(2))
