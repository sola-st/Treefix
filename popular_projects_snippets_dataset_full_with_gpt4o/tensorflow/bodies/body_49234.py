# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if isinstance(inputs, ragged_tensor.RaggedTensor):
    exit(inputs.to_tensor())
exit(inputs)
