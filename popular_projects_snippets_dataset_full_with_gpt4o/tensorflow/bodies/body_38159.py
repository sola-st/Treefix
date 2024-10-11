# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
np_ans = np_func(x).astype(dtype.as_numpy_dtype)
with test_util.force_cpu():
    self.assertAllClose(
        np_ans, self.evaluate(tf_func(ops.convert_to_tensor(x, dtype=dtype))))
