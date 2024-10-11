# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(
    ValueError, "'x' must also be initialized in the main branch"):
    self._basic_cond(lambda: variable_operators.Undefined('x'), lambda: 1)
with self.assertRaisesRegex(
    ValueError, "'x' must also be initialized in the else branch"):
    self._basic_cond(lambda: 1, lambda: variable_operators.Undefined('s'))
