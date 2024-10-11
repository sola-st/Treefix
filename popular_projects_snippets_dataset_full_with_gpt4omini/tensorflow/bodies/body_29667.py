# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.cached_session(use_gpu=use_gpu):
    tensor = ops.convert_to_tensor(tensor.astype(dtype))
    tf_ans_inv = array_ops.diag_part(tensor)
    inv_out = self.evaluate(tf_ans_inv)
self.assertAllClose(inv_out, expected_ans)
self.assertShapeEqual(expected_ans, tf_ans_inv)
