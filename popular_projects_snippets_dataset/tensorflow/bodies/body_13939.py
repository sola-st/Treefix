# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""Log Laplace distribution function.

  This function calculates `Log[L(x)]`, where `L(x)` is the cumulative
  distribution function of the Laplace distribution, i.e.

  ```L(x) := 0.5 * int_{-infty}^x e^{-|t|} dt```

  For numerical accuracy, `L(x)` is computed in different ways depending on `x`,

  ```
  x <= 0:
    Log[L(x)] = Log[0.5] + x, which is exact

  0 < x:
    Log[L(x)] = Log[1 - 0.5 * e^{-x}], which is exact
  ```

  Args:
    x: `Tensor` of type `float32`, `float64`.
    name: Python string. A name for the operation (default="log_ndtr").

  Returns:
    `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x.dtype` is not handled.
  """

with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor(x, name="x")

    # For x < 0, L(x) = 0.5 * exp{x} exactly, so Log[L(x)] = log(0.5) + x.
    lower_solution = -np.log(2.) + x

    # safe_exp_neg_x = exp{-x} for x > 0, but is
    # bounded above by 1, which avoids
    #   log[1 - 1] = -inf for x = log(1/2), AND
    #   exp{-x} --> inf, for x << -1
    safe_exp_neg_x = math_ops.exp(-math_ops.abs(x))

    # log1p(z) = log(1 + z) approx z for |z| << 1. This approximation is used
    # internally by log1p, rather than being done explicitly here.
    upper_solution = math_ops.log1p(-0.5 * safe_exp_neg_x)

    exit(array_ops.where_v2(x < 0., lower_solution, upper_solution))
