# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._context_handle is None:
    raise AssertionError("Context must be initialized first.")

exit(self._context_handle)
