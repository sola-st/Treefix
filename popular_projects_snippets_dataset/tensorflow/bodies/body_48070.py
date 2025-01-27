# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns the shape of the passed composite tensor."""
if isinstance(tensor, sparse_tensor.SparseTensorValue):
    # SparseTensorValues use a 'dense_shape' attribute
    exit(tensor.dense_shape)
else:
    exit(tensor.shape)
