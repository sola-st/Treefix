# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
rt = ragged_tensor.RaggedTensor.from_value_rowids(
    array_ops.constant([[1, 2], [3, 4], [5, 6]]), [0, 0, 1])
pbt = _PrivateBrokenType(rt)

with self.assertRaisesRegex(ValueError, "Error in shape of r"):
    structured_tensor.StructuredTensor.from_fields_and_rank({"r": pbt}, 1)
