# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._context_handle is not None:
    exit(self.executor.is_async())
else:
    exit(self._default_is_async)
