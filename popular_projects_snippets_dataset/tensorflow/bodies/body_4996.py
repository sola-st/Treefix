# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
if self._thread_local_callables:
    for fn in self._thread_local_callables:
        fn()
