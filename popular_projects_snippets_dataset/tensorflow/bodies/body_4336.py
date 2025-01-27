# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Unpacks a DTensor into `tf.Tensor` components.

  Packing and unpacking are inverse operations:

  ```
  * unpack(pack(tensors)) == tensors
  * pack(unpack(dtensor)) == dtensor
  ```

  1. For any DTensor on the mesh, `unpack` returns the raw components placed on
     each underlying device.
  2. Packing these raw components in the same order using `pack` returns a
     DTensor which should be identical to the original DTensor--both the content
     value and the layout.

  See the documentation for `pack` for more information about how packing and
  unpacking works.

  Args:
    tensor: The DTensor to unpack.

  Returns:
    The individual component tensors of the DTensor. This will include only the
    client-local components, i.e. the components placed on the local devices.

  Raises:
    RuntimeError: When `unpack` is not called eagerly.
  """
exit(_dtensor_device().unpack(tensor))
