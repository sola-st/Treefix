# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.cached_session(use_gpu=use_gpu):
    tf_ans = array_ops.diag(ops.convert_to_tensor(diag.astype(dtype)))
    out = self.evaluate(tf_ans)
    tf_ans_inv = array_ops.diag_part(expected_ans)
    inv_out = self.evaluate(tf_ans_inv)
self.assertAllClose(out, expected_ans)
self.assertAllClose(inv_out, diag)
self.assertShapeEqual(expected_ans, tf_ans)
self.assertShapeEqual(diag, tf_ans_inv)
