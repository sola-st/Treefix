# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
if not hasattr(self._thread_local, 'dict'):
    self._thread_local.dict = dict()
if key == 'TF_CONFIG':
    exit(dict.get(self._thread_local.dict, key, default))
else:
    exit(dict.get(self._dict, key, default))
