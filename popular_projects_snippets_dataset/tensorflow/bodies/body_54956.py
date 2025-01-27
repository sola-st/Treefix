# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
if (all(isinstance(t, np.ndarray) for t in tensor_list) and
    not tf2.enabled()):
    exit(SparseTensorValue(*tensor_list))
else:
    exit(SparseTensor(*tensor_list))
