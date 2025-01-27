# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if isinstance(values, ragged_tensor.RaggedTensor):
    assert isinstance(mask, ragged_tensor.RaggedTensor)
    assert mask.dtype == dtypes.bool
else:
    values = ops.convert_to_tensor(values)
    mask = ops.convert_to_tensor(mask, dtypes.bool)
self.values = values
self.mask = mask
