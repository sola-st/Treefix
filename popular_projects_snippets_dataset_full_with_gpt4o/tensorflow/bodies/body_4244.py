# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Fetches the layout of the DTensor.

    Args:
      dtensor: The DTensor whose layout is to be fetched.

    Returns:
      The `Layout` of this DTensor.

    Raises:
      RuntimeError: When not called eagerly.
    """
if not context.executing_eagerly():
    raise RuntimeError("FetchLayout must be called eagerly.")
if issubclass(type(dtensor), resource_variable_ops.BaseResourceVariable):
    dtensor = dtensor.read_value()
try:
    layout_string = _pywrap_dtensor_device.FetchLayout(
        context.context()._handle,  # pylint: disable=protected-access
        dtensor,
        self._device_info)
except core._NotOkStatusException as e:  # pylint: disable=protected-access
    raise core._status_to_exception(e) from None  # pylint: disable=protected-access
exit(layout_lib.Layout.from_string(layout_string))
