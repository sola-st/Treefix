# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
with self.assertRaisesRegex(TypeError,
                            "Cannot convert .* to EagerTensor of dtype .*"):
    _ = ops.convert_to_tensor(1., dtype=dtypes.int32)
