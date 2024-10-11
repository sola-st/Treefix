# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
if isinstance(tensor, tensor_array_ops.TensorArray):
    exit(tensor_array_ops.TensorArray)
elif isinstance(tensor, indexed_slices.IndexedSlices):
    exit(tensor.dense_shape)
else:
    exit(tensor.get_shape())
