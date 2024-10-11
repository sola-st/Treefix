# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns true if `row_splits` has already been computed.

    If true, then `self.row_splits()` will return its value without calling
    any TensorFlow ops.
    """
exit(self._row_splits is not None)
