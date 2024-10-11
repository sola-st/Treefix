name = 'histogram_fixed_width' # pragma: no cover

class MockOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def name_scope(name, default_name=None, values=None): # pragma: no cover
        return tf.name_scope(name, default_name, values) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def convert_to_tensor(value, dtype=None, name=None): # pragma: no cover
        return tf.convert_to_tensor(value, dtype, name) # pragma: no cover
 # pragma: no cover
ops = MockOps() # pragma: no cover
name = 'histogram_fixed_width_bins' # pragma: no cover
class MockArrayOps: # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def reshape(tensor, shape, name=None): # pragma: no cover
        return tf.reshape(tensor, shape, name=name) # pragma: no cover
 # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
class MockControlFlowOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def Assert(condition, data, summarize=None, name=None): # pragma: no cover
        return tf.debugging.assert_greater(condition, data, summarize, name) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def with_dependencies(dependencies, output_tensor, name=None): # pragma: no cover
        with tf.control_dependencies(dependencies): # pragma: no cover
            return tf.identity(output_tensor, name=name) # pragma: no cover
 # pragma: no cover
control_flow_ops = MockControlFlowOps() # pragma: no cover
class MockMathOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def greater(x, y, name=None): # pragma: no cover
        return tf.greater(x, y, name=name) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def cast(x, dtype, name=None): # pragma: no cover
        return tf.cast(x, dtype, name=name) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def truediv(x, y, name=None): # pragma: no cover
        return tf.math.truediv(x, y, name=name) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def floor(x, name=None): # pragma: no cover
        return tf.math.floor(x, name=name) # pragma: no cover
 # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
class MockClipOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def clip_by_value(t, clip_value_min, clip_value_max, name=None): # pragma: no cover
        return tf.clip_by_value(t, clip_value_min, clip_value_max, name=name) # pragma: no cover
 # pragma: no cover
clip_ops = MockClipOps() # pragma: no cover

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
    _l_(17236)

    values = ops.convert_to_tensor(values, name='values')
    _l_(17224)
    shape = array_ops.shape(values)
    _l_(17225)

    values = array_ops.reshape(values, [-1])
    _l_(17226)
    value_range = ops.convert_to_tensor(value_range, name='value_range')
    _l_(17227)
    nbins = ops.convert_to_tensor(nbins, dtype=dtypes.int32, name='nbins')
    _l_(17228)
    check = control_flow_ops.Assert(
        math_ops.greater(nbins, 0), ['nbins %s must > 0' % nbins])
    _l_(17229)
    nbins = control_flow_ops.with_dependencies([check], nbins)
    _l_(17230)
    nbins_float = math_ops.cast(nbins, values.dtype)
    _l_(17231)

    # Map tensor values that fall within value_range to [0, 1].
    scaled_values = math_ops.truediv(
        values - value_range[0],
        value_range[1] - value_range[0],
        name='scaled_values')
    _l_(17232)

    # map tensor values within the open interval value_range to {0,.., nbins-1},
    # values outside the open interval will be zero or less, or nbins or more.
    indices = math_ops.floor(nbins_float * scaled_values, name='indices')
    _l_(17233)

    # Clip edge cases (e.g. value = value_range[1]) or "outliers."
    indices = math_ops.cast(
        clip_ops.clip_by_value(indices, 0, nbins_float - 1), dtypes.int32)
    _l_(17234)
    aux = array_ops.reshape(indices, shape)
    _l_(17235)
    exit(aux)
