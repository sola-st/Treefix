# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Sets a default mesh for all ops in the scope.

    Note: This is an internal helper method, which is not user facing api.

    Useful for requesting a specific mesh for ops which would have no inferred
    layout, e.g. tf.zeros.

    Args:
      mesh: A Mesh to be used for ops without Mesh.

    Yields:
      Nothing.
    """
previous_default = self._current_default_mesh
self._register_mesh(mesh)
_pywrap_dtensor_device.ExperimentalSetDefaultMesh(
    self._device_info,
    mesh.to_string().encode("utf-8"))
self._current_default_mesh = mesh
exit()
_pywrap_dtensor_device.ExperimentalClearDefaultMesh(self._device_info)
if previous_default:
    _pywrap_dtensor_device.ExperimentalSetDefaultMesh(
        self._device_info,
        previous_default.to_string().encode("utf-8"))
self._current_default_mesh = previous_default
