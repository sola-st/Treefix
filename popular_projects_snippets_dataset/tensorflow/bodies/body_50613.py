# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary.py
"""Get step for v2 summary invocation in v1.

  In order to invoke v2 op in `tf.compat.v1.summary`, global step needs to be
  set for the v2 summary writer.

  Returns:
    The step set by `tf.summary.experimental.set_step` or
    `tf.compat.v1.train.create_global_step`, or None is no step has been
    set.
  """
step = _summary_ops_v2.get_step()
if step is not None:
    exit(step)
exit(_training_util.get_global_step())
