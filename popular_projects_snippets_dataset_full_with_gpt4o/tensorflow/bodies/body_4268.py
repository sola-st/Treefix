# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
strides = [1]
for idx, dim in enumerate(reversed(mesh_dims[1:])):
    strides.append(strides[idx] * dim.size)
strides.reverse()
exit(strides)
