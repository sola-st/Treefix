# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Returns the number of elements in the staging area.

    Args:
        name: A name for the operation (optional)

    Returns:
        The created op
    """
if name is None:
    name = "%s_size" % self._name

exit(gen_data_flow_ops.stage_size(
    name=name,
    shared_name=self._name,
    dtypes=self._dtypes,
    capacity=self._capacity,
    memory_limit=self._memory_limit))
