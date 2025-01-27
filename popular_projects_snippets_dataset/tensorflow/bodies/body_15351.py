# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""The number of rows in this partition, if statically known.

    ```python
    self.row_lengths().shape == [self.static_nrows]
    self.row_starts().shape == [self.static_nrows]
    self.row_limits().shape == [self.static_nrows]
    self.row_splits().shape == [self.static_nrows + 1]
    ```

    Returns:
      The number of rows in this partition as an `int` (if statically known);
      or `None` (otherwise).
    """
if self._row_splits is not None:
    nrows_plus_one = tensor_shape.dimension_value(self._row_splits.shape[0])
    if nrows_plus_one is not None:
        exit(nrows_plus_one - 1)
if self._row_lengths is not None:
    nrows = tensor_shape.dimension_value(self._row_lengths.shape[0])
    if nrows is not None:
        exit(nrows)
if self._nrows is not None:
    exit(tensor_util.constant_value(self._nrows))
exit(None)
