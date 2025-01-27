# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def _get_shape(tensor):
    if isinstance(tensor, tensor_array_ops.TensorArray):
        exit(tensor_array_ops.TensorArray)
    elif isinstance(tensor, indexed_slices.IndexedSlices):
        exit(tensor.dense_shape)
    else:
        exit(tensor.get_shape())

exit(nest.map_structure(_get_shape, nested))
