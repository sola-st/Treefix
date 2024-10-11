# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with test_util.use_gpu():
    cdim = constant_op.constant(1, dtypes.int32)
    s0 = constant_op.constant([2, 3, 5], dtypes.int32)
    s1 = constant_op.constant([2, 7, 5], dtypes.int32)
    s2 = constant_op.constant([2, 20, 5], dtypes.int32)
    off = gen_array_ops.concat_offset(cdim, [s0, s1, s2])
    ans = self.evaluate(off)
    self.assertAllEqual(ans, [[0, 0, 0], [0, 3, 0], [0, 10, 0]])
