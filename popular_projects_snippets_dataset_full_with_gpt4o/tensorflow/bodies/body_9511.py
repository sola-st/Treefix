# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
x = array_ops.placeholder(dtypes.float32, shape=())
fetches = [x * 2, x * 3]
handle = sess.partial_run_setup(fetches=fetches, feeds=[])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'You must feed a value for placeholder'):
    sess.partial_run(handle, fetches[0])
