# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
"""Synchronous training across multiple replicas on one machine.

    Args:
      mesh: optional DTensor mesh for the computation. Note that either `mesh`
        or `devices` should be provided, and not both. The mesh should be 1D,
        and will be used to split the input data among that dimension.
      devices: a list of device strings, such as ['/gpu:0', '/gpu:1']. If both
        `mesh` and `devices` are None, all the available GPU/TPU will be used.
        If no accelerators are found, CPU is used.
      cross_device_ops: optional, a descendant of `CrossDeviceOps`. The value is
        ignored at the moment, and support will be added later.
    """
self._validate_init_args(mesh, devices)
if not mesh:
    mesh = self._build_mesh_from_device_list(devices)

extended = MirroredExtended(container_strategy=self, mesh=mesh)
super().__init__(extended)
self._mesh = mesh
self._devices = devices
