# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
np_ans = np.array(x)
with context.device("/device:CPU:0"):
    tf_ans = ops.convert_to_tensor(x).numpy()
if np_ans.dtype in [np.float32, np.float64, np.complex64, np.complex128]:
    self.assertAllClose(np_ans, tf_ans)
else:
    self.assertAllEqual(np_ans, tf_ans)
