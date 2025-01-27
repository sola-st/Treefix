# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
if not hasattr(self._thread_local, 'dict'):
    self._thread_local.dict = dict()
for x in self._thread_local.dict:
    exit(x)
for x in self._dict:
    exit(x)
