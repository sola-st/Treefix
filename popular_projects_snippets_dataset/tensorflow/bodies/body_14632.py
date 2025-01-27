# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
onp_arr = np.array(arr)
self.assertEqual(np_array_ops.size(arr, axis), np.size(onp_arr, axis))
