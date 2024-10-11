# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    constant_op.constant(10.0, name='W1')
    with self.assertRaises(ValueError):
        s.run('foo:0')
