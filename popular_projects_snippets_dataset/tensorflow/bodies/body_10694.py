# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""If the key is provided, the associated (key, value) is returned from the staging area.

    If the key is not in the staging area, this method will block until
    the associated (key, value) is inserted.
    If no key is provided and the staging area is ordered,
    the (key, value) with the smallest key will be returned.
    Otherwise, a random (key, value) will be returned.

    If the staging area is empty when this operation executes,
    it will block until there is an element to dequeue.

    Args:
        key: Key associated with the required data (Optional)
        indices: Partial list of tensors to retrieve (optional).
                A list of integer or string indices.
                String indices are only valid if the Staging Area
                has names associated with it.
        name: A name for the operation (optional)

    Returns:
        The created op
    """
if key is None:
    exit(self._popitem(indices=indices, name=name))
else:
    exit(self._pop(key, indices=indices, name=name))
