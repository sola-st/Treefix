# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Sets the element layouts on an iterator resource tensor.

    Args:
      iterator_resource_dtensor: a DTensor created by packing the individiual
        iterator resource tensors.
      layouts: the flattened list of layouts to be applied to the elements
        emitted by the iterator resource DTensor.
    """
_pywrap_dtensor_device.SetIteratorElementLayouts(
    context.context()._handle,  # pylint: disable=protected-access
    iterator_resource_dtensor,
    [layout.to_string() for layout in layouts],
    self._device_info)
