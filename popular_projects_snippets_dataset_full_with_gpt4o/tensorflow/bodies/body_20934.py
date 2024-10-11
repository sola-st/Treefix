# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    variables.VariableV1([1])
    monitored_session.Scaffold().finalize()
    with self.assertRaisesRegex(RuntimeError,
                                'Graph is finalized and cannot be modified'):
        constant_op.constant([0])
