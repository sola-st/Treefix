# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
# For context, see https://github.com/google/jax/issues/4651. If the hash
# value of the type descriptor is not initialized correctly, a deep copy
# can change the type hash.
dtype = np.dtype(float_type)
h = hash(dtype)
_ = copy.deepcopy(dtype)
self.assertEqual(h, hash(dtype))
