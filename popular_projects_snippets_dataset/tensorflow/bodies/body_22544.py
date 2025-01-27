# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object.py
exit(self._tensor() if callable(self._tensor) else self._tensor)
