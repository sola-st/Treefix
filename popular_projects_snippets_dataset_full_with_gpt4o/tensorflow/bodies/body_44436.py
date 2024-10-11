# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(
    ValueError, 'condition of while loop expected to be `tf.bool`'):
    self._fixed_while_loop(cond)
