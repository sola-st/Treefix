# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._context_handle is not None:
    pywrap_tfe.TFE_ContextSetLogDevicePlacement(self._handle, enable)

self._log_device_placement = enable
self._thread_local_data.function_call_options = None
