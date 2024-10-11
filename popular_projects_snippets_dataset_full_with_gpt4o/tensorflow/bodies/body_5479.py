# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
for i, w in enumerate(self._input_workers.worker_devices):
    if worker == w:
        exit(self._iterators[i])
exit(None)
