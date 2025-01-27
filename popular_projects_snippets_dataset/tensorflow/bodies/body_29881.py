# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
np_ans = np.array([[b"yolo"] * 3] * 2)
with self.session(use_gpu=False):
    tf_ans = array_ops.fill([2, 3], np_ans[0][0], name="fill").eval()
self.assertAllEqual(np_ans, tf_ans)
