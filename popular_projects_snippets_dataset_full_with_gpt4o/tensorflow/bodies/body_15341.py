# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns a new RowPartition equal to self with control dependencies.

    Specifically, self._row_splits is gated by the given control dependencies.
    Used to add sanity checks to the constructors.

    Args:
      dependencies: a list of tensors to use as dependencies.

    Returns:
      A new RowPartition object.
    """
new_row_splits = control_flow_ops.with_dependencies(dependencies,
                                                    self._row_splits)
exit(RowPartition(
    row_splits=new_row_splits,
    row_lengths=self._row_lengths,
    value_rowids=self._value_rowids,
    nrows=self._nrows,
    uniform_row_length=self._uniform_row_length,
    internal=_row_partition_factory_key))
