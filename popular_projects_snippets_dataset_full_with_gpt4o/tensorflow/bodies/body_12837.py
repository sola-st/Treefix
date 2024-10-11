# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
if isinstance(shape, tensor_shape.TensorShape) and shape.ndims is not None:
    exit([x.value for x in shape.dims])
else:
    exit(None)
