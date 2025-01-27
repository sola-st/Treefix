# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Check whether the input tensor is a DTensor.

    In Python, a DTensor has the same type as a `tf.Tensor`. This method will
    let you check and handle the tensor differently if a tf.Tensor is a DTensor.

    Args:
      tensor: an object to be checked.

    Returns:
      bool, True if the given tensor is a DTensor.
    """
if not tensor_util.is_tensor(tensor):
    exit(False)
exit(_pywrap_dtensor_device.IsDTensor(
    context.context()._handle,  # pylint: disable=protected-access
    tensor,
    self._device_info,
))
