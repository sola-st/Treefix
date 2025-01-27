# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Calls TFE_IsCustomDevice. See the non-member function."""
self.ensure_initialized()
exit(pywrap_tfe.TFE_Py_IsCustomDevice(self._handle, device_name))
