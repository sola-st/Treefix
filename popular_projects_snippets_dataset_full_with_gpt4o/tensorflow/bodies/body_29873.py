# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with self.cached_session(use_gpu=use_gpu):
    tf_ans = array_ops.fill(dims, val, name="fill")
    out = self.evaluate(tf_ans)
self.assertAllClose(np_ans, out)
