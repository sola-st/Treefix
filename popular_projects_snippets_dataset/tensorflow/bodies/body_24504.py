# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get all the downstream consumers of this op.

    Only data (non-control) edges are tracked.

    Args:
      src_op_name: Name of the op providing the tensor being consumed.

    Returns:
      A list of (src_slot, dst_op_name, dst_slot) tuples. In each item of
      the list:
        src_slot: 0-based output slot of the op of which the output tensor
          is being consumed.
        dst_op_name: Name of the consuming op (e.g., "Conv2D_3/BiasAdd")
        dst_slot: 0-based input slot of the consuming op that receives
          the tensor from this op.
    """
exit(self._op_consumers[src_op_name])
