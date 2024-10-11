# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(tuple(v.device for v in self._values))
