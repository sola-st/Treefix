# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random_test.py
np.random.seed(1)
np.random.seed(np.int32(1))
with self.assertRaises(ValueError):
    np.random.seed((1, 3))
