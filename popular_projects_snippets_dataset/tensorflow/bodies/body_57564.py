# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Returns a list of the names of the input tensors.

    Returns:
      List of strings.
    """
if self._has_valid_tensors():
    exit([_get_tensor_name(tensor) for tensor in self._input_tensors])
else:
    exit([name for name, _ in self._input_arrays_with_shape])
