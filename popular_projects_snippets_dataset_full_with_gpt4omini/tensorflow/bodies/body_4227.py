# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
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
