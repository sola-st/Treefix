# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(ValueError, "'s' is not allowed to be None"):
    self._basic_loop(None, lambda i, s: s)
with self.assertRaisesRegex(ValueError, "'s' must be defined"):
    self._basic_loop(variable_operators.Undefined(''), lambda i, s: s)
