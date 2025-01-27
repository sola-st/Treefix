# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
arr = np.asarray([10.])

# TODO(nareshmodi): Test more ops.
sq = onp.square(arr)
self.assertIsInstance(sq, onp.ndarray)
self.assertEqual(100., sq[0])
