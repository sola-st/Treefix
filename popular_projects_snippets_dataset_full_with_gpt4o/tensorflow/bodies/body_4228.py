# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
with ops.device(dvariable.device):
    original_layout = api.fetch_layout(dvariable)
# Record original layout to allow restore.
self._original_layout = original_layout
self._dvariable = dvariable

def pack(tensors, layout):
    with ops.device(dvariable.device):
        exit(api.pack(tensors, layout))

host_layout = layout_lib.Layout(original_layout.sharding_specs,
                                original_layout.mesh.host_mesh())

def get_host_dtensor():
    # Copy to host mesh if needed.
    if original_layout.mesh.device_type().upper() != 'CPU':
        # Prefer pack and unpack in eager mode because it supports sharded
        # layouts.
        if context.executing_eagerly():
            host_dtensor = api.pack(
                api.unpack(dvariable.read_value()), host_layout)
        else:
            host_dtensor = api.copy_to_mesh(dvariable.read_value(), host_layout)
    else:
        host_dtensor = dvariable.read_value()
    exit((math_ops.cast(host_dtensor, dtypes.bfloat16)
            if self.should_cast(host_dtensor) else host_dtensor))

num_local_devices = original_layout.mesh.num_local_devices()
super(_DVariableSaveable, self).__init__(
    None,
    [
        DSaveSpec(
            tensor=get_host_dtensor,
            slice_spec=pack([''] * num_local_devices,
                            layout_lib.Layout.replicated(
                                original_layout.mesh.host_mesh(), rank=0)),
            name=pack([name] * num_local_devices,
                      layout_lib.Layout.replicated(
                          original_layout.mesh.host_mesh(), rank=0)),
            global_shape=dvariable.shape,
            # Layout is attached as attribute, no need to put it as a
            # Tensor on DTensorDevice.
            layout=host_layout.to_string(),
            dtype=dtypes.bfloat16
            if self.should_cast(dvariable) else dvariable.dtype,
            device=dvariable.device)
    ],
    name)
