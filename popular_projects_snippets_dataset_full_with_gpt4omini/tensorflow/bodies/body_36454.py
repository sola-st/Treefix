# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)
ret = while_loop_v2(
    lambda v: v < 8., lambda v: v * v, [x], return_same_structure=True)
grad = gradients_impl.gradients(ret, [x])
with self.cached_session() as sess:
    eval_result = sess.run(ret)
    self.assertIsInstance(eval_result, list)
    self.assertLen(eval_result, 1)
    self.assertEqual(16., eval_result[0])
    self.assertSequenceEqual(sess.run(grad), [32.])
