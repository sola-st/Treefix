# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Closes this barrier.

    This operation signals that no more new key values will be inserted in the
    given barrier. Subsequent InsertMany operations with new keys will fail.
    InsertMany operations that just complement already existing keys with other
    components, will continue to succeed. Subsequent TakeMany operations will
    continue to succeed if sufficient elements remain in the barrier. Subsequent
    TakeMany operations that would block will fail immediately.

    If `cancel_pending_enqueues` is `True`, all pending requests to the
    underlying queue will also be canceled, and completing of already
    started values is also not acceptable anymore.

    Args:
      cancel_pending_enqueues: (Optional.) A boolean, defaulting to
        `False` (described above).
      name: Optional name for the op.

    Returns:
      The operation that closes the barrier.
    """
if name is None:
    name = "%s_BarrierClose" % self._name
exit(gen_data_flow_ops.barrier_close(
    self._barrier_ref,
    cancel_pending_enqueues=cancel_pending_enqueues,
    name=name))
