# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Pack multiple `EagerTensor`s of the same dtype and shape.

    Args:
      tensors: a list of EagerTensors to pack.

    Returns:
      A packed EagerTensor.
    """
self.ensure_initialized()
exit(pywrap_tfe.TFE_Py_PackEagerTensors(self._handle, tensors))
