# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Creates a new partitioned variable wrapper.

    Variables passed via the variable_list must contain a save_slice_info
    field.  Concatenation and iteration is in lexicographic order according
    to the var_offset property of the save_slice_info.

    Args:
      name: String. Overall name of the variables.
      shape: List of integers.  Overall shape of the variables.
      dtype: Type of the variables.
      variable_list: List of `Variable` that comprise this partitioned variable.
      partitions: List of integers.  Number of partitions for each dimension.

    Raises:
      TypeError: If `variable_list` is not a list of `Variable` objects, or
        `partitions` is not a list.
      ValueError: If `variable_list` is empty, or the `Variable` shape
        information does not match `shape`, or `partitions` has invalid values.
    """
if not isinstance(variable_list, (list, tuple)):
    raise TypeError("variable_list is not a list or tuple: %s" %
                    variable_list)
if not isinstance(partitions, (list, tuple)):
    raise TypeError("partitions is not a list or tuple: %s" % partitions)
if not all(p >= 1 for p in partitions):
    raise ValueError("partition values must be positive: %s" % partitions)
if not variable_list:
    raise ValueError("variable_list may not be empty")
# pylint: disable=protected-access
for v in variable_list:
    # Sort the variable_list lexicographically according to var offset value.
    if not all(v._get_save_slice_info() is not None for v in variable_list):
        raise ValueError(
            "All variables must have a save_slice_info available: %s" %
            [v.name for v in variable_list])
    if len(shape) != len(partitions):
        raise ValueError("len(shape) != len(partitions): %s vs. %s" %
                         (shape, partitions))
    if v._get_save_slice_info().full_shape != shape:
        raise ValueError("All variables' full shapes must match shape: %s; "
                         "but full shapes were: %s" %
                         (shape, str([v._get_save_slice_info().full_shape])))
self._variable_list = sorted(
    variable_list, key=lambda v: v._get_save_slice_info().var_offset)
# pylint: enable=protected-access

self._name = name
self._shape = shape
self._dtype = dtype
self._partitions = partitions
self._as_tensor = None
