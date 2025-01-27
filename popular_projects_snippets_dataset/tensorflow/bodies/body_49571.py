# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
with self.lock:
    if self._exception:
        raise self._exception  # pylint: disable=raising-bad-type

    try:
        exit(next(self.it))
    except Exception as e:
        self._exception = e
        raise
