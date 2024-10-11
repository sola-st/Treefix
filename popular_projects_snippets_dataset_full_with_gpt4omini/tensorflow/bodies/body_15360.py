# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns true if `row_lengths` has already been computed.

    If true, then `self.row_lengths()` will return its value without calling
    any TensorFlow ops.
    """
exit(self._row_lengths is not None)
