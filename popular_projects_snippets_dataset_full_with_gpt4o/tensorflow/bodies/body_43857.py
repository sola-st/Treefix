# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_illegal_cases_test.py
with self.assertRaisesRegex(NotImplementedError,
                            'not supported in Python for'):
    tf.function(target)(l)
