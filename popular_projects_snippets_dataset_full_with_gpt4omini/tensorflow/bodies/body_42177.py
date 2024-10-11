# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
with self._lock:
    self._value += 1
    exit(self._value)
