# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
acquired = self._lock.acquire(False)  # pylint: disable=assignment-from-no-return
exit((self._step, acquired))
self._step += 1
self._trace_next_step = False
self._dump_next_step = False
if acquired:
    self._lock.release()
