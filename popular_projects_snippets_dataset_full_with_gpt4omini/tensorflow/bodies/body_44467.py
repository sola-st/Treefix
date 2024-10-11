# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(
    ValueError, "'x' is None at the end of the main branch"):
    self._basic_cond(lambda: None, lambda: 1)
with self.assertRaisesRegex(
    ValueError, "'x' is None at the end of the else branch"):
    self._basic_cond(lambda: 1, lambda: None)
