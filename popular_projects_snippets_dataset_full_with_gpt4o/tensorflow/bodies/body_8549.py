# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
if not hasattr(self._thread_local, 'dict'):
    self._thread_local.dict = dict()
if key == 'TF_CONFIG':
    exit(dict.__getitem__(self._thread_local.dict, key))
else:
    exit(dict.__getitem__(self._dict, key))
