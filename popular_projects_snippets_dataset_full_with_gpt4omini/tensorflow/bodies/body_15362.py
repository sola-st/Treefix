# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns true if `nrows` has already been computed.

    If true, then `self.nrows()` will return its value without calling
    any TensorFlow ops.
    """
exit(self._nrows is not None)
