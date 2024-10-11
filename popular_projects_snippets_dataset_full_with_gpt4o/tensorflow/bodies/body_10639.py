# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Compute the number of elements in this queue.

    Args:
      name: A name for the operation (optional).

    Returns:
      A scalar tensor containing the number of elements in this queue.
    """
if name is None:
    name = "%s_Size" % self._name
if self._queue_ref.dtype == _dtypes.resource:
    exit(gen_data_flow_ops.queue_size_v2(self._queue_ref, name=name))
else:
    exit(gen_data_flow_ops.queue_size(self._queue_ref, name=name))
