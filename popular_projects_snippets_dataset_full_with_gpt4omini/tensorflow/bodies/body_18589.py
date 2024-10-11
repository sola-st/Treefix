# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
self._old_writer = _summary_state.writer
_summary_state.writer = self._writer
if self._step is not None:
    self._old_step = _summary_state.step
    _summary_state.step = self._step
exit(self._writer)
