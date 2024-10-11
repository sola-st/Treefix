# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
tf_ans = self.evaluate(array_ops.slice(x, [begin, 0], [size, x.shape[1]]))
np_ans = x[begin:begin + size, :]
self.assertAllEqual(tf_ans, np_ans)
