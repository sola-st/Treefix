# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
a = ops.convert_to_tensor(value=a, dtype=np.int32)
b = ops.convert_to_tensor(value=b, dtype=np.int32)
if not isinstance(out, np_arrays.ndarray):
    out = ops.convert_to_tensor(value=out, dtype=np.int32)
if types is None:
    types = [[np.int32, np.int32, np.int32], [np.int64, np.int32, np.int64],
             [np.int32, np.int64, np.int64],
             [np.float32, np.int32, np.float64],
             [np.int32, np.float32, np.float64],
             [np.float32, np.float32, np.float32],
             [np.float64, np.float32, np.float64],
             [np.float32, np.float64, np.float64]]
for a_type, b_type, out_type in types:
    o = f(a.astype(a_type), b.astype(b_type))
    self.assertIs(o.dtype.as_numpy_dtype, out_type)
    out = out.astype(out_type)
    if np.issubdtype(out_type, np.inexact):
        self.assertAllClose(out, o)
    else:
        self.assertAllEqual(out, o)
