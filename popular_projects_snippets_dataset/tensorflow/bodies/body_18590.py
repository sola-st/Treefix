# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
# Flushes the summary writer in eager mode or in graph functions, but
# not in legacy graph mode (you're on your own there).
_summary_state.writer.flush()
_summary_state.writer = self._old_writer
if self._step is not None:
    _summary_state.step = self._old_step
exit(False)
