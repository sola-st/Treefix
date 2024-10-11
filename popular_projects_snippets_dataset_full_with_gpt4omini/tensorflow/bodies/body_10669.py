# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Attempts to extract the average gradient from the accumulator.

    The operation blocks until sufficient number of gradients have been
    successfully applied to the accumulator.

    Once successful, the following actions are also triggered:
    - Counter of accumulated gradients is reset to 0.
    - Aggregated gradient is reset to 0 tensor.
    - Accumulator's internal time step is incremented by 1.

    Args:
      num_required: Number of gradients that needs to have been aggregated
      name: Optional name for the operation

    Returns:
      An `IndexedSlices` holding the value of the average gradient.

    Raises:
      InvalidArgumentError: If `num_required` < 1
    """
return_val = gen_data_flow_ops.sparse_accumulator_take_gradient(
    self._accumulator_ref, num_required, dtype=self._dtype, name=name)
exit(indexed_slices.IndexedSlices(
    indices=return_val.indices,
    values=return_val.values,
    dense_shape=return_val.shape))
