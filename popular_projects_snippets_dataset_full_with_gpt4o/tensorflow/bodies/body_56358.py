# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
with self.assertRaisesRegex(ValueError, "not compatible"):
    tensor_spec.BoundedTensorSpec((3, 5), dtypes.uint8, (0, 0, 0), (1, 1))
