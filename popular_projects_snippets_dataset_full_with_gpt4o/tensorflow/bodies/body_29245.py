# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
if isinstance(v, tensor_array_ops.TensorArray):
    exit(v.stack())
exit(v)
