# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
with self.cached_session(use_gpu=use_gpu):
    if raises is not None:
        with self.assertRaises(raises):
            array_ops.one_hot(dtype=dtype, **inputs)
    else:
        ans = array_ops.one_hot(dtype=dtype, **inputs)
        if expected_err_re is None:
            tf_ans = self.evaluate(ans)
            self.assertAllEqual(tf_ans, truth)
            if dtype:
                self.assertEqual(tf_ans.dtype, dtype)
            self.assertEqual(tf_ans.shape, ans.get_shape())
        else:
            with self.assertRaisesOpError(expected_err_re):
                self.evaluate(ans)
