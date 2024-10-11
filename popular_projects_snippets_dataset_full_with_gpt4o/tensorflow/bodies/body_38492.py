# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/argmax_op_test.py
with self.session(use_gpu=use_gpu):
    ans = method(x, axis=axis)
    if expected_err_re is None:
        tf_ans = self.evaluate(ans)
        # Defaults to int64 output.
        self.assertEqual(np.int64, tf_ans.dtype)
        self.assertAllEqual(tf_ans, expected_values)
        self.assertShapeEqual(expected_values, ans)
    else:
        with self.assertRaisesOpError(expected_err_re):
            self.evaluate(ans)
