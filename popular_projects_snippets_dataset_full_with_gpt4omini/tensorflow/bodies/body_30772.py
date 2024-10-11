# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
with test_util.use_gpu():
    tf_ans = array_ops.bitcast(x, datatype)
    out = self.evaluate(tf_ans)
    buff_after = memoryview(out).tobytes()
    buff_before = memoryview(x).tobytes()
    self.assertEqual(buff_before, buff_after)
    self.assertEqual(tf_ans.get_shape(), shape)
    self.assertEqual(tf_ans.dtype, datatype)
