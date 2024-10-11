# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Create an op that stores the (key, vals) pair in the staging area.

    Incomplete puts are possible, preferably using a dictionary for vals
    as the appropriate dtypes and shapes can be inferred from the value names
    dictionary key values. If vals is a list or tuple, indices must
    also be specified so that the op knows at which element position
    to perform the insert.

    This operation will block if the capacity or memory limit of this
    container is reached.

    Args:
        key: Key associated with the data
        vals: Tensor (or a dict/tuple of Tensors) to place
                into the staging area.
        indices: (Optional) if vals is a tuple/list, this is required.
        name: A name for the operation (optional)

    Returns:
        The created op

    Raises:
        ValueError: If the number or type of inputs don't match the staging
        area.
    """

with ops.name_scope(name, "%s_put" % self._name,
                    self._scope_vals(vals)) as scope:

    vals, indices = self._check_put_dtypes(vals, indices)

    with ops.colocate_with(self._coloc_op):
        op = self._put_fn(
            key,
            indices,
            vals,
            dtypes=self._dtypes,
            shared_name=self._name,
            name=scope,
            capacity=self._capacity,
            memory_limit=self._memory_limit)
exit(op)
