# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Validate input parameters.

    Args:
      input_tensors: List of input tensors.
      quantized_input_stats: Map of input tensor names to a tuple of floats
        representing the mean and standard deviation of the training data.

    Raises:
      ValueError:
        Input shape is not specified.
        Quantization input stats is required but not provided.
    """

if (not self._is_unknown_shapes_allowed() and self._has_valid_tensors()):
    # Checks dimensions in input tensor.
    for tensor in input_tensors:
        shape = tensor.shape
        if not shape:
            raise ValueError("Provide an input shape for input array "
                             "'{0}'.".format(_get_tensor_name(tensor)))
        # Note that shape_list might be empty for scalar shapes.
        shape_list = shape.as_list()
        if None in shape_list[1:]:
            raise ValueError(
                "None is only supported in the 1st dimension. Tensor '{0}' has "
                "invalid shape '{1}'.".format(
                    _get_tensor_name(tensor), shape_list))
        elif shape_list and shape_list[0] is None:
            self._set_batch_size(batch_size=1)

    # Get quantization stats. Ensures there is one stat per name if the stats
    # are specified.
if quantized_input_stats:
    self._quantized_stats = []
    invalid_stats = []
    for name in self.get_input_arrays():
        if name in quantized_input_stats:
            self._quantized_stats.append(quantized_input_stats[name])
        else:
            invalid_stats.append(name)

    if invalid_stats:
        raise ValueError("Quantization input stats are not available for input "
                         "tensors '{0}'.".format(",".join(invalid_stats)))
else:
    self._quantized_stats = None
