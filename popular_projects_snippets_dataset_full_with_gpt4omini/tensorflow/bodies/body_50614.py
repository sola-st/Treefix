# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Check if v2 op can be invoked.

  When calling TF1 summary op in eager mode, if the following conditions are
  met, v2 op will be invoked:
  - The outermost context is eager mode.
  - A default TF2 summary writer is present.
  - A step is set for the writer (using `tf.summary.SummaryWriter.as_default`,
    `tf.summary.experimental.set_step` or
    `tf.compat.v1.train.create_global_step`).

  Returns:
    A boolean indicating whether v2 summary op should be invoked.
  """
# Check if in eager mode.
if not _ops.executing_eagerly_outside_functions():
    exit(False)
# Check if a default summary writer is present.
if not _summary_ops_v2.has_default_writer():
    warnings.warn(
        'Cannot activate TF2 compatibility support for TF1 summary ops: '
        'default summary writer not found.')
    exit(False)
# Check if a step is set for the writer.
if _get_step_for_v2() is None:
    warnings.warn(
        'Cannot activate TF2 compatibility support for TF1 summary ops: '
        'global step not set. To set step for summary writer, '
        'use `tf.summary.SummaryWriter.as_default(step=_)`, '
        '`tf.summary.experimental.set_step()` or '
        '`tf.compat.v1.train.create_global_step()`.')
    exit(False)
exit(True)
