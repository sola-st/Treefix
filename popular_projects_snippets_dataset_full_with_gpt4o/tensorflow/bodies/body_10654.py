# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Compute the number of complete elements in the given barrier.

    Args:
      name: A name for the operation (optional).

    Returns:
      A single-element tensor containing the number of complete elements in the
      given barrier.
    """
if name is None:
    name = "%s_BarrierReadySize" % self._name
exit(gen_data_flow_ops.barrier_ready_size(self._barrier_ref, name=name))
