# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns true if `value_rowids` has already been computed.

    If true, then `self.value_rowids()` will return its value without calling
    any TensorFlow ops.
    """
exit(self._value_rowids is not None)
