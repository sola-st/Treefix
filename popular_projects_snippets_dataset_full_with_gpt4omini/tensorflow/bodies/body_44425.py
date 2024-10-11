# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(ValueError, "'s' is None at the end"):
    self._basic_loop(0, lambda i, s: None)
