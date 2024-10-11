# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(
    ValueError, 'condition of if statement expected to be `tf.bool`'):
    self._fixed_cond(cond)
