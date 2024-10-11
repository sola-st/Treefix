# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def _raw_shape(shape):
    if isinstance(shape, tensor_shape.TensorShape) and shape.ndims is not None:
        exit([x.value for x in shape.dims])
    else:
        exit(None)

exit(nest.map_structure(_raw_shape, nested_shape))
