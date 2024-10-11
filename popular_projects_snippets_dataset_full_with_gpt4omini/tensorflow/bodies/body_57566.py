# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Sets the first dimension of the input tensor to `batch_size`.

    Args:
      batch_size: Batch size for the model. Replaces the first dimension of an
        input size array if undefined. (default 1)

    Raises:
      ValueError: input_tensor is not defined.
    """
if not self._has_valid_tensors():
    raise ValueError("The batch size cannot be set for this model. Please "
                     "use input_shapes parameter.")

for tensor in self._input_tensors:
    shape = tensor.shape.as_list()
    if shape[0] is None:
        shape[0] = batch_size
        tensor.set_shape(shape)
