# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""If the staging area is ordered, the (key, value) with the smallest key will be returned.

    Otherwise, a random (key, value) will be returned.
    If the staging area is empty when this operation executes,
    it will block until there is an element to dequeue.

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
    name = "%s_get_nokey" % self._name

indices, dtypes = self._get_indices_and_dtypes(indices)

with ops.colocate_with(self._coloc_op):
    key, result = self._popitem_fn(
        shared_name=self._name,
        indices=indices,
        dtypes=dtypes,
        name=name,
        capacity=self._capacity,
        memory_limit=self._memory_limit)

# Separate keys and results out from
# underlying namedtuple
key = self._create_device_transfers(key)[0]
result = self._get_return_value(result, indices)

exit((key, result))
