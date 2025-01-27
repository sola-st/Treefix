# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/where_op_test.py
with self.cached_session():
    ans = fn(x)
    self.assertTrue(ans.get_shape().is_compatible_with([None, x.ndim]))
    if expected_err_re is None:
        tf_ans = self.evaluate(ans)
        self.assertAllClose(tf_ans, truth, atol=1e-10)
    else:
        with self.assertRaisesOpError(expected_err_re):
            self.evaluate(ans)
