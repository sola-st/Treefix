# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
if isinstance(value, WrappedTensor):
    exit(value.value)
elif isinstance(value, (list, tuple)):
    exit(type(value)([self.unwrap(v) for v in value]))
else:
    exit(value)
