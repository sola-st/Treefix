# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
np_ans = np.array([[b"yolo"] * 3] * 2)
tf_ans = array_ops.fill([2, 3], np_ans[0][0], name="fill").numpy()
self.assertAllEqual(np_ans, tf_ans)
