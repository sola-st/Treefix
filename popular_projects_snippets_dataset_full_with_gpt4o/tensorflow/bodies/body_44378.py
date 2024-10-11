# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(TypeError, '\'s\'.* dtype float32 after'):
    self._basic_loop(0, lambda i, s: 1.0)
