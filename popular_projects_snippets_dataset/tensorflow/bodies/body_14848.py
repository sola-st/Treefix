# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
a = np_array_ops.array(6, dtype=np.int8)
b = np_array_ops.array(22, dtype=np.int8)
res_tf = np_math_ops.lcm(a, b)
res_np = np.lcm(np.array(a), np.array(b))
self.assertEqual(res_tf, res_np)
