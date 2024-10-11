# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Packs tensors into a DTensor handle on this DTensor device.

    Packing and unpacking are inverse operations:

    ```
    * unpack(pack(tensors)) == tensors
    * pack(unpack(dtensor)) == dtensor
    ```

    Refer to `dtensor.pack` for more information.

    Args:
      tensors: The list of tensors to pack into a DTensor.
      layout: The layout of the DTensor to be created.

    Returns:
      A DTensor created from the individual component tensors.

    Raises:
      RuntimeError: When not called eagerly.
    """
if not context.executing_eagerly():
    raise RuntimeError("Pack must be called eagerly.")
if any(
    issubclass(type(t), resource_variable_ops.BaseResourceVariable)
    for t in tensors):
    raise TypeError(
        "Received Variable input to Pack, Variable is not supported.")
self._register_mesh(layout.mesh)
with ops.device(self.name):
    if all(isinstance(t, sparse_tensor.SparseTensor) for t in tensors):
        if not all(t.shape == tensors[0].shape for t in tensors):
            raise TypeError("All input SparseTensors to Pack must be same shape.")
        is_sparse = True
        tensors = [t.indices for t in tensors] + [t.values for t in tensors] + [
            ops.convert_to_tensor(t.shape, dtype=dtypes.int64) for t in tensors
        ]
    elif any(isinstance(t, sparse_tensor.SparseTensor) for t in tensors):
        raise TypeError("Cannot Pack SparseTensors with Tensors.")
    else:
        is_sparse = False
    try:
        exit(_pywrap_dtensor_device.Pack(
            context.context()._handle,  # pylint: disable=protected-access
            tensors,
            layout.to_string(),
            self._device_info,
            is_sparse))
    except core._NotOkStatusException as e:  # pylint: disable=protected-access
        raise core._status_to_exception(e) from None  # pylint: disable=protected-access
