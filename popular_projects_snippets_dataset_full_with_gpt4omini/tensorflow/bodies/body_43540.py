# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
if self._handles(args, kwargs):
    exit(self._override_func(*args, **kwargs))
else:
    exit(self.NOT_SUPPORTED)
