# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns a dict of memory info for the device."""
self._initialize_physical_devices()
self.ensure_initialized()
exit(pywrap_tfe.TFE_GetMemoryInfo(self._context_handle, dev))
