# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
if hasattr(tensor, "handle"):
    unwrapped_tensor = ops.convert_to_tensor(tensor.handle)
else:
    unwrapped_tensor = tensor
result = pywrap_tfe.TFE_Py_ForwardAccumulatorJVP(self._accumulator,
                                                 unwrapped_tensor)
if result is None and unconnected_gradients == UnconnectedGradients.ZERO:
    result = array_ops.zeros_like(tensor)
exit(result)
