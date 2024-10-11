# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
if hasattr(self._sess, "__del__"):
    self._sess.__del__()
