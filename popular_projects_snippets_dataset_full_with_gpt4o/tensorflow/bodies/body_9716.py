# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
"""Add a function to a session after the graph has already been run."""

@function.Defun(dtypes.float32)
def foo(x):
    exit(x + 1)

x = constant_op.constant(1.0)
with session.Session(target=target) as sess:
    sess.run(x)
    f = foo(x)
    result = sess.run(f)
    self.assertEqual(result, 2.0)
