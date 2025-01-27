# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
super().__init__(
    tensor=tensor,
    slice_spec=slice_spec,
    name=name,
    dtype=dtype,
    device=device)
self.global_shape = global_shape
self.layout = layout
