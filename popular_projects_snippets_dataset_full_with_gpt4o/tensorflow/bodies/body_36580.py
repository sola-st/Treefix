# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with ops.device("/cpu:0"):
    x = constant_op.constant(0)
    ret, = while_loop_v2(lambda x: x < 1000, lambda x: x + 1, [x])
with self.cached_session(config=config):
    self.assertEqual(1000, self.evaluate(ret))
