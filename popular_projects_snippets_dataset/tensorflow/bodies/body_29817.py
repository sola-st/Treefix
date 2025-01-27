# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
np_ans = np.array(x)
with self.cached_session():
    tf_ans = ops.convert_to_tensor(x).eval()
dtype = dtypes_lib.as_dtype(np_ans.dtype)
if dtype.is_floating or dtype.is_complex:
    self.assertAllClose(np_ans, tf_ans)
else:
    self.assertAllEqual(np_ans, tf_ans)
