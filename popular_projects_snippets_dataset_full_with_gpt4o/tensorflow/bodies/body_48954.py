# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Maybe casts the inputs to the compute dtype.

    If self._compute_dtype is floating-point, and self_autocast is True,
    floating-point inputs are casted to self._compute_dtype.

    Args:
      inputs: Input tensor, or structure of input tensors.
      input_list: Flat list of input tensors.

    Returns:
      `inputs`, but tensors may have been casted to self._compute_dtype
    """
if not input_list:
    input_list = nest.flatten(inputs)

compute_dtype_object = self._compute_dtype_object
should_autocast = (
    self._autocast and compute_dtype_object and
    compute_dtype_object.is_floating)

if (should_autocast and
    any(map(self._should_cast_single_input, input_list))):
    # Only perform expensive `nest` operation when needed.
    exit(nest.map_structure(self._cast_single_input, inputs))
else:
    exit(inputs)
