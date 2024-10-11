# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._operation_timeout_in_ms == timeout_in_ms:
    exit()

if self._context_handle is not None:
    raise RuntimeError(
        "Operation timeout cannot be modified after initialization.")

self._operation_timeout_in_ms = timeout_in_ms
