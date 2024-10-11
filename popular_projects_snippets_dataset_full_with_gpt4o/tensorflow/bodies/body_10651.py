# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""For each key, assigns the respective value to the specified component.

    This operation updates each element at component_index.

    Args:
      component_index: The component of the value that is being assigned.
      keys: A vector of keys, with length n.
      values: An any-dimensional tensor of values, which are associated with the
        respective keys. The first dimension must have length n.
      name: Optional name for the op.

    Returns:
      The operation that performs the insertion.
    Raises:
      InvalidArgumentsError: If inserting keys and values without elements.
    """
if name is None:
    name = "%s_BarrierInsertMany" % self._name
exit(gen_data_flow_ops.barrier_insert_many(
    self._barrier_ref, keys, values, component_index, name=name))
