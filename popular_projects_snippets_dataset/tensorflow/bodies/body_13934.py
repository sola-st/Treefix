# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""Log Normal distribution function.

  For details of the Normal distribution function see `ndtr`.

  This function calculates `(log o ndtr)(x)` by either calling `log(ndtr(x))` or
  using an asymptotic series. Specifically:
  - For `x > upper_segment`, use the approximation `-ndtr(-x)` based on
    `log(1-x) ~= -x, x << 1`.
  - For `lower_segment < x <= upper_segment`, use the existing `ndtr` technique
    and take a log.
  - For `x <= lower_segment`, we use the series approximation of erf to compute
    the log CDF directly.

  The `lower_segment` is set based on the precision of the input:

  ```
  lower_segment = { -20,  x.dtype=float64
                  { -10,  x.dtype=float32
  upper_segment = {   8,  x.dtype=float64
                  {   5,  x.dtype=float32
  ```

  When `x < lower_segment`, the `ndtr` asymptotic series approximation is:

  ```
     ndtr(x) = scale * (1 + sum) + R_N
     scale   = exp(-0.5 x**2) / (-x sqrt(2 pi))
     sum     = Sum{(-1)^n (2n-1)!! / (x**2)^n, n=1:N}
     R_N     = O(exp(-0.5 x**2) (2N+1)!! / |x|^{2N+3})
  ```

  where `(2n-1)!! = (2n-1) (2n-3) (2n-5) ...  (3) (1)` is a
  [double-factorial](https://en.wikipedia.org/wiki/Double_factorial).


  Args:
    x: `Tensor` of type `float32`, `float64`.
    series_order: Positive Python `integer`. Maximum depth to
      evaluate the asymptotic expansion. This is the `N` above.
    name: Python string. A name for the operation (default="log_ndtr").

  Returns:
    log_ndtr: `Tensor` with `dtype=x.dtype`.

  Raises:
    TypeError: if `x.dtype` is not handled.
    TypeError: if `series_order` is a not Python `integer.`
    ValueError:  if `series_order` is not in `[0, 30]`.
  """
if not isinstance(series_order, int):
    raise TypeError("series_order must be a Python integer.")
if series_order < 0:
    raise ValueError("series_order must be non-negative.")
if series_order > 30:
    raise ValueError("series_order must be <= 30.")

with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor(x, name="x")

    if x.dtype.as_numpy_dtype == np.float64:
        lower_segment = LOGNDTR_FLOAT64_LOWER
        upper_segment = LOGNDTR_FLOAT64_UPPER
    elif x.dtype.as_numpy_dtype == np.float32:
        lower_segment = LOGNDTR_FLOAT32_LOWER
        upper_segment = LOGNDTR_FLOAT32_UPPER
    else:
        raise TypeError("x.dtype=%s is not supported." % x.dtype)

    # The basic idea here was ported from:
    #   https://root.cern.ch/doc/v608/SpecFuncCephesInv_8cxx_source.html
    # We copy the main idea, with a few changes
    # * For x >> 1, and X ~ Normal(0, 1),
    #     Log[P[X < x]] = Log[1 - P[X < -x]] approx -P[X < -x],
    #     which extends the range of validity of this function.
    # * We use one fixed series_order for all of 'x', rather than adaptive.
    # * Our docstring properly reflects that this is an asymptotic series, not a
    #   Taylor series. We also provided a correct bound on the remainder.
    # * We need to use the max/min in the _log_ndtr_lower arg to avoid nan when
    #   x=0. This happens even though the branch is unchosen because when x=0
    #   the gradient of a select involves the calculation 1*dy+0*(-inf)=nan
    #   regardless of whether dy is finite. Note that the minimum is a NOP if
    #   the branch is chosen.
    exit(array_ops.where_v2(
        math_ops.greater(x, upper_segment),
        -_ndtr(-x),  # log(1-x) ~= -x, x << 1  # pylint: disable=invalid-unary-operand-type
        array_ops.where_v2(
            math_ops.greater(x, lower_segment),
            math_ops.log(_ndtr(math_ops.maximum(x, lower_segment))),
            _log_ndtr_lower(math_ops.minimum(x, lower_segment), series_order))))
