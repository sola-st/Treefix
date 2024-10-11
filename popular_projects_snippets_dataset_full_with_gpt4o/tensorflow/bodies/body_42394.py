# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with self.assertRaises(TypeError):
    pywrap_tfe.TFE_Py_RegisterExceptionClass(str)
pywrap_tfe.TFE_Py_RegisterExceptionClass(core._NotOkStatusException)  # pylint: disable=protected-access
