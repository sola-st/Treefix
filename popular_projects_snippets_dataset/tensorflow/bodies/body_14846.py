# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
with self.assertRaisesRegex(ValueError, r''):
    np_math_ops.matmul(
        np_array_ops.ones([], np.int32), np_array_ops.ones([2, 3], np.int32))
with self.assertRaisesRegex(ValueError, r''):
    np_math_ops.matmul(
        np_array_ops.ones([2, 3], np.int32), np_array_ops.ones([], np.int32))
