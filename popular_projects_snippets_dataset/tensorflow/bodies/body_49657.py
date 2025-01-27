# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns true if `tensor` is a ragged tensor or ragged tensor value."""
exit(isinstance(
    tensor,
    (ragged_tensor.RaggedTensor, ragged_tensor_value.RaggedTensorValue)))
