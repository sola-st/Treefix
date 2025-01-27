# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Returns true if queue is closed.

    This operation returns true if the queue is closed and false if the queue
    is open.

    Args:
      name: A name for the operation (optional).

    Returns:
      True if the queue is closed and false if the queue is open.
    """
if name is None:
    name = "%s_Is_Closed" % self._name
if self._queue_ref.dtype == _dtypes.resource:
    exit(gen_data_flow_ops.queue_is_closed_v2(self._queue_ref, name=name))
else:
    exit(gen_data_flow_ops.queue_is_closed_(self._queue_ref, name=name))
