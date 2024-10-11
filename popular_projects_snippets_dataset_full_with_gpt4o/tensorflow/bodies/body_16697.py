# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Constructor.

    Args:
      full_shape: Tuple or list of `int` indicating the full combined shape of
        the partitioned variables.
      var_offset: Tuple or list of `int` specifying offset of this partition
        with respect to the full variable for each dimension.

    Raises:
      TypeError: If `full_shape` or `var_offset` is not a sequence.
      ValueError: If `full_shape` or `var_offset` differ in length. If
        `var_offset` exceeds `full_shape` in any dimension.
    """
if not isinstance(full_shape, (list, tuple)):
    raise TypeError(
        "`full_shape` must be a sequence (like tuple or list) instead of " +
        type(full_shape).__name__)

if not isinstance(var_offset, (list, tuple)):
    raise TypeError(
        "`var_offset` must be a sequence (like tuple or list) instead of " +
        type(var_offset).__name__)

if len(var_offset) != len(full_shape):
    raise ValueError(
        "Expected equal length, but `var_offset` is of length {} while "
        "full_shape is of length {}.".format(
            len(var_offset), len(full_shape)))

for offset, shape in zip(var_offset, full_shape):
    if offset < 0 or offset >= shape:
        raise ValueError(
            "Expected 0 <= offset < shape but found offset={}, shape={} for "
            "var_offset={}, full_shape={}".format(offset, shape, var_offset,
                                                  full_shape))

self._full_shape = full_shape
self._var_offset = var_offset
