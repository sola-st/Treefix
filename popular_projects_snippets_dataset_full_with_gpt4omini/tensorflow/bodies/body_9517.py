# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
sess = session.Session()
x = array_ops.placeholder(dtypes.float32, shape=[])
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'specify at least one target to fetch or execute.'):
    sess.partial_run_setup(fetches=[], feeds=[x])
