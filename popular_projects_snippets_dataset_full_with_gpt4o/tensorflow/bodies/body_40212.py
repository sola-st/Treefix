# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
if not self._recording:
    raise ValueError("Accumulator is not recording.")
pywrap_tfe.TFE_Py_ForwardAccumulatorSetRemove(self._accumulator)
self._recording = False
