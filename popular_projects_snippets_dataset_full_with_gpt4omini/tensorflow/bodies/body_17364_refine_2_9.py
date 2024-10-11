import numpy as np # pragma: no cover

name = 'histogram_test' # pragma: no cover

name = 'histogram_fixed_width' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/histogram_ops.py
from l3.Runtime import _l_
"""Bins the given values for use in a histogram.

  Given the tensor `values`, this operation returns a rank 1 `Tensor`
  representing the indices of a histogram into which each element
  of `values` would be binned. The bins are equal width and
  determined by the arguments `value_range` and `nbins`.

  Args:
    values:  Numeric `Tensor`.
    value_range:  Shape [2] `Tensor` of same `dtype` as `values`.
      values <= value_range[0] will be mapped to hist[0],
      values >= value_range[1] will be mapped to hist[-1].
    nbins:  Scalar `int32 Tensor`.  Number of histogram bins.
    dtype:  dtype for returned histogram.
    name:  A name for this operation (defaults to 'histogram_fixed_width').

  Returns:
    A `Tensor` holding the indices of the binned values whose shape matches
    `values`.

  Raises:
    TypeError: If any unsupported dtype is provided.
    tf.errors.InvalidArgumentError: If value_range does not
        satisfy value_range[0] < value_range[1].

  Examples:

  >>> # Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
  ...
  >>> nbins = 5
  >>> value_range = [0.0, 5.0]
  >>> new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]
  >>> indices = tf.histogram_fixed_width_bins(new_values, value_range, nbins=5)
  >>> indices.numpy()
  array([0, 0, 1, 2, 4, 4], dtype=int32)
  """
with ops.name_scope(name, 'histogram_fixed_width_bins',
                    [values, value_range, nbins]):
    _l_(5497)

    values = ops.convert_to_tensor(values, name='values')
    _l_(5485)
    shape = array_ops.shape(values)
    _l_(5486)

    values = array_ops.reshape(values, [-1])
    _l_(5487)
    value_range = ops.convert_to_tensor(value_range, name='value_range')
    _l_(5488)
    nbins = ops.convert_to_tensor(nbins, dtype=dtypes.int32, name='nbins')
    _l_(5489)
    check = control_flow_ops.Assert(
        math_ops.greater(nbins, 0), ['nbins %s must > 0' % nbins])
    _l_(5490)
    nbins = control_flow_ops.with_dependencies([check], nbins)
    _l_(5491)
    nbins_float = math_ops.cast(nbins, values.dtype)
    _l_(5492)

    # Map tensor values that fall within value_range to [0, 1].
    scaled_values = math_ops.truediv(
        values - value_range[0],
        value_range[1] - value_range[0],
        name='scaled_values')
    _l_(5493)

    # map tensor values within the open interval value_range to {0,.., nbins-1},
    # values outside the open interval will be zero or less, or nbins or more.
    indices = math_ops.floor(nbins_float * scaled_values, name='indices')
    _l_(5494)

    # Clip edge cases (e.g. value = value_range[1]) or "outliers."
    indices = math_ops.cast(
        clip_ops.clip_by_value(indices, 0, nbins_float - 1), dtypes.int32)
    _l_(5495)
    aux = array_ops.reshape(indices, shape)
    _l_(5496)
    exit(aux)
