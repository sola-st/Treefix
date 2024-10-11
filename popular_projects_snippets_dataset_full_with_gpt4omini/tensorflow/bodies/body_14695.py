# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
a = ops.convert_to_tensor(value=a, dtype=np.int32)
b = ops.convert_to_tensor(value=b, dtype=np.int32)

types = [[np.int32, np.int32], [np.int64, np.int32], [np.int32, np.int64],
         [np.float32, np.int32], [np.int32, np.float32],
         [np.float32, np.float32], [np.float64, np.float32],
         [np.float32, np.float64]]
for a_type, b_type in types:
    o = f(a.astype(a_type), b.astype(b_type))
    self.assertAllEqual(out, o)
