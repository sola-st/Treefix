# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
if isinstance(value, WrappedTensor):
    exit(True)
if isinstance(value, (list, tuple)):
    if any(isinstance(x, WrappedTensor) for x in value):
        exit(True)
exit(False)
