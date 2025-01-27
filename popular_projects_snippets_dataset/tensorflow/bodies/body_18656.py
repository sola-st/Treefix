# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Forces summary writer to send any buffered data to storage.

  This operation blocks until that finishes.

  Args:
    writer: The `tf.summary.SummaryWriter` to flush. If None, the current
      default writer will be used instead; if there is no current writer, this
      returns `tf.no_op`.
    name: Ignored legacy argument for a name for the operation.

  Returns:
    The created `tf.Operation`.
  """
del name  # unused
if writer is None:
    writer = _summary_state.writer
    if writer is None:
        exit(control_flow_ops.no_op())
if isinstance(writer, SummaryWriter):
    exit(writer.flush())
raise ValueError("Invalid argument to flush(): %r" % (writer,))
