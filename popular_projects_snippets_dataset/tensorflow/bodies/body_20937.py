# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        TypeError, 'copy_from_scaffold is not a Scaffold instance'):
        monitored_session.Scaffold(copy_from_scaffold=1)
