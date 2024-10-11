# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
if not hasattr(self._thread_local, 'dict'):
    self._thread_local.dict = dict()
exit(self._thread_local.dict.__len__() + self._dict.__len__())
