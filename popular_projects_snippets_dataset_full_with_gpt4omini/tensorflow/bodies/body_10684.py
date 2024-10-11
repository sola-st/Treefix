# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Create an op that places a value into the staging area.

    This operation will block if the `StagingArea` has reached
    its capacity.

    Args:
      values: A single tensor, a list or tuple of tensors, or a dictionary with
        tensor values. The number of elements must match the length of the
        list provided to the dtypes argument when creating the StagingArea.
      name: A name for the operation (optional).

    Returns:
        The created op.

    Raises:
      ValueError: If the number or type of inputs don't match the staging area.
    """
with ops.name_scope(name, "%s_put" % self._name,
                    self._scope_vals(values)) as scope:

    if not isinstance(values, (list, tuple, dict)):
        values = [values]

    # Hard-code indices for this staging area
    indices = list(range(len(values)))
    vals, _ = self._check_put_dtypes(values, indices)

    with ops.colocate_with(self._coloc_op):
        op = gen_data_flow_ops.stage(
            values=vals,
            shared_name=self._name,
            name=scope,
            capacity=self._capacity,
            memory_limit=self._memory_limit)

    exit(op)
