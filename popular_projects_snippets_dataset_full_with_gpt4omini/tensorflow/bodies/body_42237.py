# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Calls TFE_RegisterCustomDevice. See the non-member function."""
self.ensure_initialized()
pywrap_tfe.TFE_Py_RegisterCustomDevice(self._handle, device_capsule,
                                       device_name, device_info_capsule)
