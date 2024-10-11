# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Indicate that a summary was computed.

    Args:
      sess: A `Session` object.
      summary: A Summary proto, or a string holding a serialized summary proto.
      global_step: Int. global step this summary is associated with. If `None`,
        it will try to fetch the current step.

    Raises:
      TypeError: if 'summary' is not a Summary proto or a string.
      RuntimeError: if the Supervisor was created without a `logdir`.
    """
if not self._summary_writer:
    raise RuntimeError("Writing a summary requires a summary writer.")
if global_step is None and self.global_step is not None:
    global_step = training_util.global_step(sess, self.global_step)
self._summary_writer.add_summary(summary, global_step)
