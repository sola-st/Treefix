# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
if self._sv.global_step is not None:
    summary_strs, global_step = self._sess.run(
        [self._sv.summary_op, self._sv.global_step])
else:
    summary_strs = self._sess.run(self._sv.summary_op)
    global_step = None
if self._sv.summary_writer:
    logging.info("Recording summary at step %s.", global_step)
    self._sv.summary_writer.add_summary(summary_strs, global_step)
