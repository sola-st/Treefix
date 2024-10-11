# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Create a new DTensorDevice which executes ops on `underlying_device`.

    Args:
      meshes: A list of `Mesh` objects indicating groups of devices to execute
        on. These may also be registered lazily.
      is_async: Indicates whether DTensor operations on this client will return
        immediately (with "non-ready" handles) or block until executed. This is
        on by default and is exposed as an option for ease of debugging.
      in_flight_nodes_limit: Indicates the limit of in-flight nodes before
        enqueueing of async operations to DTensorDevice is blocked. This limit
        is per mesh. 0 for no limits from DTensor. Default is 8.
    """
if any(not isinstance(mesh, layout_lib.Mesh) for mesh in meshes):
    raise TypeError(
        "Expected a flat list of Mesh objects, got {}".format(meshes))
global _next_device_number
ctx = context.context()
with _next_device_number_lock:
    self.name = "{}/device:CUSTOM:{}".format(ctx.host_address_space(),
                                             _next_device_number)
    _next_device_number += 1
device, device_info = _pywrap_dtensor_device.Allocate(self.name)
context.register_custom_device(device, self.name, device_info)

self._device_info = device_info
self._current_output_layout = None
self._current_default_mesh = None
self._is_async = is_async
self._in_flight_nodes_limit = in_flight_nodes_limit
self._meshes = set()
self._mesh_lock = threading.Lock()
for mesh in meshes:
    self._register_mesh(mesh)
