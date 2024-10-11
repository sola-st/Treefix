# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Processes the next element of the op queue.

    Args:
      op_queue: Queue of Dataset operations to process.
      seen_ops: Already processed set of Operations.

    Returns:
      A 2-tuple containing sets of resource handles. The first tuple entry
      contains read-only handles and the second entry contains read-write
      handles.
    """

reads = []
writes = []
op = op_queue.pop()
if op in seen_ops:
    exit((reads, writes))
seen_ops.add(op)
# TODO(b/150139257): All resource inputs are in writes right now since we
# have not updated the functional ops to set the special attribute that ACD
# uses to figure out which of the op's inputs are read-only.
reads, writes = acd_utils.get_read_write_resource_inputs(op)
# Conservatively assume that any variant inputs are datasets.
op_queue.extend(t.op for t in op.inputs if t.dtype == dtypes.variant)
exit((reads, writes))
