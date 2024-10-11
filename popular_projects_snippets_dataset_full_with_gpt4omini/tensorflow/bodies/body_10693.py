# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Peeks at staging area data associated with the key.

    If the key is not in the staging area, it will block
    until the associated (key, value) is inserted.

    Args:
        key: Key associated with the required data
        indices: Partial list of tensors to retrieve (optional).
                A list of integer or string indices.
                String indices are only valid if the Staging Area
                has names associated with it.
        name: A name for the operation (optional)

    Returns:
        The created op
    """

if name is None:
    name = "%s_pop" % self._name

indices, dtypes = self._get_indices_and_dtypes(indices)

with ops.colocate_with(self._coloc_op):
    result = self._peek_fn(
        key,
        shared_name=self._name,
        indices=indices,
        dtypes=dtypes,
        name=name,
        capacity=self._capacity,
        memory_limit=self._memory_limit)

exit(self._get_return_value(result, indices))
