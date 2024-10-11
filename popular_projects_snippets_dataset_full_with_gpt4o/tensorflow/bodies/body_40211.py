# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
if self._recording:
    raise ValueError("Accumulator is already recording.")
pywrap_tfe.TFE_Py_ForwardAccumulatorSetAdd(self._accumulator)
self._recording = True
