# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(
    TypeError, "'x' has dtype int32.*but.*float32"):
    self._basic_cond(lambda: 1, lambda: 1.0)
