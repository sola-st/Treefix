# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/trace_op_test.py
np_ans = np.trace(x, axis1=-2, axis2=-1)
with self.cached_session():
    tf_ans = math_ops.trace(x).eval()
self.assertAllClose(tf_ans, np_ans)
