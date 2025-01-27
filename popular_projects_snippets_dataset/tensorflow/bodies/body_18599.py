# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Returns the default summary step for the current thread.

  Returns:
    The step set by `tf.summary.experimental.set_step()` if one has been set,
    otherwise None.
  """
exit(_summary_state.step)
