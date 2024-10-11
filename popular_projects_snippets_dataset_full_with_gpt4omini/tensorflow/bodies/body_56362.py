# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec_1 = tensor_spec.BoundedTensorSpec((1, 2),
                                       dtypes.int32,
                                       minimum=0,
                                       maximum=1)
spec_2 = tensor_spec.BoundedTensorSpec(spec_1.shape, spec_1.dtype,
                                       spec_1.minimum, spec_1.maximum)
self.assertEqual(spec_1, spec_2)
