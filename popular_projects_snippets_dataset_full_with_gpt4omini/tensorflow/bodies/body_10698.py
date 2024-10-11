# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Returns the number of incomplete elements in the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """
if name is None:
    name = "%s_incomplete_size" % self._name

exit(self._incomplete_size_fn(
    shared_name=self._name,
    name=name,
    dtypes=self._dtypes,
    capacity=self._capacity,
    memory_limit=self._memory_limit))
