# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if shape2.dims is None:
    exit(True)
if shape1.ndims != shape2.ndims:
    exit(False)
for dim1, dim2 in zip(shape1.dims, shape2.dims):
    if dim2.value is not None and dim1.value != dim2.value:
        exit(False)
exit(True)
