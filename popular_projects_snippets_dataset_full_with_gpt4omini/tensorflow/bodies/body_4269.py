# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Builds a Mesh.

    The `dim_names` and `global_device_ids` arguments describe the dimension
    names and shape for the mesh.

    For example,

    ```python
      dim_names = ('x', 'y'),
      global_device_ids = [[0, 1],
                           [2, 3],
                           [4, 5]]
    ```

    defines a 2D mesh of shape 3x2. A reduction over the 'x' dimension will
    reduce across columns (0, 2, 4) and (1, 3, 5), and a reduction over the 'y'
    dimension reduces across rows.

    Note: the utilities `dtensor.create_mesh` and
    `dtensor.create_distributed_mesh` provide a simpler API to create meshes for
    single- or multi-client use cases.

    Args:
      dim_names: A list of strings indicating dimension names.
      global_device_ids: An ndarray of global device IDs is used to compose
        DeviceSpecs describing the mesh. The shape of this array determines the
        size of each mesh dimension. Values in this array should increment
        sequentially from 0. This argument is the same for every DTensor client.
      local_device_ids: A list of local device IDs equal to a subset of values
        in global_device_ids. They indicate the position of local devices in the
        global mesh. Different DTensor clients must contain distinct
        local_device_ids contents. All local_device_ids from all DTensor clients
        must cover every element in global_device_ids.
      local_devices: The list of devices hosted locally. The elements correspond
        1:1 to those of local_device_ids.
      mesh_name: The name of the mesh. Currently, this is rarely used, and is
        mostly used to indicate whether it is a CPU, GPU, or TPU-based mesh.
      global_devices (optional): The list of global devices. Set when multiple
        device meshes are in use.
      use_xla_spmd (optional): Boolean when True, will use XLA SPMD instead of
        DTensor SPMD.
    """
# Check if input args are valid.
if not isinstance(global_device_ids, np.ndarray):
    raise ValueError('Variable global_device_ids must be an ndarray.')
if global_device_ids.size == 0:
    raise ValueError('Variable global_device_ids must be non-empty.')
flat_global_device_ids = global_device_ids.flatten()
# global_device_ids are expected to be consecutive numbers.
# LINT.IfChange
distance = flat_global_device_ids[0]
if any(
    (gid - i != distance) for i, gid in enumerate(flat_global_device_ids)):
    raise ValueError('global_device_ids must sequentially increase: %s' %
                     global_device_ids)
# LINT.ThenChange(//tensorflow/dtensor/cc/dtensor_device.cc)

# TODO(b/242201545): This class is only for args type transformation for
# exported C++ Mesh class after the unification is complete. Any other
# logics should reside in the C++ layer.

# Transform args format for C++ Mesh constructor
global_device_ids_flatten = global_device_ids.flatten()
global_device_ids_shape = global_device_ids.shape
local_devices_str = [d.to_string() for d in local_devices]
if global_devices:
    global_devices_str = [d.to_string() for d in global_devices]
else:
    global_devices_str = []

super().__init__(mesh_name, dim_names, global_device_ids_shape,
                 global_device_ids_flatten, global_devices_str,
                 local_device_ids, local_devices_str, use_xla_spmd)

if len(dim_names) != global_device_ids.ndim:
    raise ValueError(
        'Number of mesh dimensions does not match number of dimension names.')

if not isinstance(local_device_ids, list):
    raise ValueError('Variable local_device_ids must be a list of integers.')

if not isinstance(local_devices, list):
    raise ValueError('Variable local_devices must be a list of DeviceSpecs.')

if global_devices and not isinstance(global_devices, list):
    raise ValueError('Variable global_devices must be a list of DeviceSpecs.')

if not local_devices and not global_devices:
    raise ValueError('Empty list of devices not allowed.')

local_devices_set = set(local_devices)
local_device_only_contains_host_cpu = (
    len(local_devices_set) == 1 and
    list(local_devices_set)[0].device_type == 'CPU')
if not local_device_only_contains_host_cpu and len(local_devices) != len(
    local_devices_set):
    raise ValueError('Duplicate devices found in mesh specification %s.' %
                     [d for d in local_devices if local_devices.count(d) > 1])

if len(local_device_ids) != len(local_devices):
    raise ValueError(
        'Variable local_device_ids does not have same size as local_devices.')

if len(local_device_ids) > len(np.ravel(global_device_ids)):
    raise ValueError('Cannot have more local than gobal device IDs.')

device_types = set([device.device_type for device in local_devices])
if not device_types:
    device_types = set([device.device_type for device in global_devices])
if None in device_types:
    raise ValueError('device_type is required')
if len(device_types) > 1:
    raise ValueError('Devices containing multiple device_types : %s' %
                     device_types)
device_type = device_types.pop()
if use_xla_spmd and device_type != 'TPU':
    raise ValueError('XLA SPMD is not currently not supported for %s mesh.' %
                     device_type)
# Set object's state.
self._device_type = device_type
self._dim_names = dim_names
self._dim_dict = {
    dim_name: MeshDimension(dim_name, global_device_ids.shape[i])
    for i, dim_name in enumerate(dim_names)
}
self._global_device_ids = global_device_ids
self._local_device_ids = local_device_ids
self._local_devices = local_devices
self._global_devices = global_devices
self._name = mesh_name
self._strides = _compute_mesh_strides(
    [self._dim_dict[dim] for dim in self._dim_names])
self._use_xla_spmd = use_xla_spmd
