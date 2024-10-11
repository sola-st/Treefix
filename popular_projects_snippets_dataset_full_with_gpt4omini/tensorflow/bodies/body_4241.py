# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Copy `tensor` to `device` with the given layout."""
self._register_mesh(new_layout.mesh)
with ops.device(self.name):
    exit(gen_dtensor_ops.copy_to_mesh(tensor, layout=new_layout.to_string()))
