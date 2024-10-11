# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
for dtype in [
    dtypes.float16,
    dtypes.float32,
    dtypes.float64,
    dtypes.bfloat16,
    dtypes.int16,
    dtypes.int32,
    dtypes.int64,
    dtypes.uint8,
]:
    with self.cached_session():
        x = constant_op.constant([1, 2, 3, 4, 5, 6], shape=[2, 3], dtype=dtype)
        np_ans = [[4, 4, 4], [4, 5, 6]]
        clip_value_min = 4
        clip_value_max = constant_op.constant(
            [6, 6, 6, 6, 6, 6], shape=[2, 3], dtype=dtype)
        ans = clip_ops.clip_by_value(x, clip_value_min, clip_value_max)
        tf_ans = self.evaluate(ans)

    self.assertAllClose(np_ans, tf_ans)
