# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/convert_to_tensor_or_ragged_tensor_op_test.py
rt = ragged_factory_ops.constant(pylist)
converted = ragged_tensor.convert_to_tensor_or_ragged_tensor(
    rt, dtype, preferred_dtype)
self.assertIs(converted, rt)
