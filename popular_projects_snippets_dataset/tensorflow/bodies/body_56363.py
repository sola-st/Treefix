# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
spec = tensor_spec.BoundedTensorSpec((),
                                     dtypes.float32,
                                     minimum=0.0,
                                     maximum=1.0)

self.assertIsInstance(spec.minimum, np.ndarray)
self.assertIsInstance(spec.maximum, np.ndarray)

# Sanity check that numpy compares correctly to a scalar for an empty shape.
self.assertEqual(0.0, spec.minimum)
self.assertEqual(1.0, spec.maximum)

# Check that the spec doesn't fail its own input validation.
_ = tensor_spec.BoundedTensorSpec(spec.shape, spec.dtype, spec.minimum,
                                  spec.maximum)
