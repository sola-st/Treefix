# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Compute the number of incomplete elements in the given barrier.

    Args:
      name: A name for the operation (optional).

    Returns:
      A single-element tensor containing the number of incomplete elements in
      the given barrier.
    """
if name is None:
    name = "%s_BarrierIncompleteSize" % self._name
exit(gen_data_flow_ops.barrier_incomplete_size(
    self._barrier_ref, name=name))
