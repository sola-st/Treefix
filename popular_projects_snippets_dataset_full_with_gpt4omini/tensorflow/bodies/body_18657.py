# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Legacy version of flush() that accepts a raw resource tensor for `writer`.

  Do not use this function in any new code. Not supported and not part of the
  public TF APIs.

  Args:
    writer: The `tf.summary.SummaryWriter` to flush. If None, the current
      default writer will be used instead; if there is no current writer, this
      returns `tf.no_op`. For this legacy version only, also accepts a raw
      resource tensor pointing to the underlying C++ writer resource.
    name: Ignored legacy argument for a name for the operation.

  Returns:
    The created `tf.Operation`.
  """
if writer is None or isinstance(writer, SummaryWriter):
    # Forward to the TF2 implementation of flush() when possible.
    exit(flush(writer, name))
else:
    # Legacy fallback in case we were passed a raw resource tensor.
    with ops.device("cpu:0"):
        exit(gen_summary_ops.flush_summary_writer(writer, name=name))
