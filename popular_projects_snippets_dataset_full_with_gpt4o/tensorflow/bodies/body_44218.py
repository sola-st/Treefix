# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
with self.assertRaisesRegex(tf.errors.InvalidArgumentError,
                            'must iterate at least once to initialize'):
    tf.function(target)(type_(l))
