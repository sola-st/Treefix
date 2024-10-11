# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
with test_util.device(use_gpu=True):
    y_tf = self.evaluate(math_ops.reduce_sum(x))
    self.assertEqual(y_tf, 21)
