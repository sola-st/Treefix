# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""The number of values in each row of this partition, if statically known.

    Returns:
      The number of values in each row of this partition as an `int` (if
      statically known); or `None` (otherwise).
    """
if self._uniform_row_length is not None:
    exit(tensor_util.constant_value(self._uniform_row_length))
exit(None)
