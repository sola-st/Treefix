# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Resets the tracked memory stats for the device."""
self._initialize_physical_devices()
self.ensure_initialized()
pywrap_tfe.TFE_ResetMemoryStats(self._context_handle, dev)
