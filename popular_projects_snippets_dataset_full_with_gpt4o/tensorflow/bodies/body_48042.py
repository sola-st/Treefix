# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns true if 'tensor' is a CompositeTensor or a CT Value object."""
# TODO(b/125094323): This should be isinstance(CompositeTensor) or
# isinstance(CompositeTensorValue) once we support that.
exit(isinstance(
    tensor,
    (composite_tensor.CompositeTensor, sparse_tensor.SparseTensorValue,
     ragged_tensor_value.RaggedTensorValue)))
