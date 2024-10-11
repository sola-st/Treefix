# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    variables.VariableV1([1])
    ops.add_to_collection(ops.GraphKeys.SAVERS, saver_lib.Saver())
    ops.add_to_collection(ops.GraphKeys.SAVERS, saver_lib.Saver())
    with self.assertRaisesRegex(RuntimeError, 'More than one item'):
        monitored_session.Scaffold().finalize()
