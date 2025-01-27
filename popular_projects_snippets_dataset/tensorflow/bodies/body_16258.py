# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
components = list(components)
value = components.pop()
while components:
    value = ragged_tensor_value.RaggedTensorValue(value, components.pop())
exit(value)
