# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
x = np.random.rand(3, 3)
i = np.arange(3)
expected_ans = x[i, i]
for shape in None, (None, 3), (3, None):
    with self.cached_session(use_gpu=False):
        t = ops.convert_to_tensor(x.astype(np.float32))
        t.set_shape(shape)
        tf_ans = array_ops.diag_part(t)
        out = self.evaluate(tf_ans)
    self.assertAllClose(out, expected_ans)
    self.assertShapeEqual(expected_ans, tf_ans)
