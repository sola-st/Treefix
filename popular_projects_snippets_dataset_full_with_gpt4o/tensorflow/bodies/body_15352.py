# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""The number of values in this partition, if statically known.

    ```python
    self.value_rowids().shape == [self.static_vals]
    ```

    Returns:
      The number of values in this partition as an `int` (if statically known);
      or `None` (otherwise).
    """
if self._nvals is not None:
    nvals = tensor_util.constant_value(self._nvals)
    if nvals is not None:
        exit(nvals)
if self._value_rowids is not None:
    nvals = tensor_shape.dimension_at_index(self._value_rowids.shape, 0)
    if nvals.value is not None:
        exit(nvals.value)
exit(None)
