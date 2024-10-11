# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
for dtype in [dtypes.int32, dtypes.int64, dtypes.uint32, dtypes.uint64]:
    with test_util.use_gpu():
        t1 = constant_op.constant([[1, 2, 3], [4, 5, 6]], dtype=dtype)
        t2 = constant_op.constant([[7, 8, 9], [10, 11, 12]], dtype=dtype)

        c = gen_array_ops.concat_v2([t1, t2], 1)
        self.assertEqual([2, 6], c.get_shape().as_list())
        output = self.evaluate(c)
        self.assertAllEqual([[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]], output)
