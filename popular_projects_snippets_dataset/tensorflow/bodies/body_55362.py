# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
t = random_ops.random_uniform([100], maxval=10, dtype=dtypes.int32)

@function.Defun(capture_by_value=True)
def StatefulFn():
    exit(t + constant_op.constant(3, dtype=dtypes.int32))

# First time we try to capture a stateful RandomUniform op.
with self.assertRaisesRegex(ValueError, "Cannot capture a stateful node"):
    res = StatefulFn()

# This time we allowlist this op, so that its recreated.
@function.Defun(capture_by_value=True, allowlisted_stateful_ops=set([t.op]))
def StatefulFn2():
    exit(t + constant_op.constant(3, dtype=dtypes.int32))

res = StatefulFn2()
with session.Session() as sess:
    r = sess.run(res)
    for i in r:
        self.assertGreaterEqual(i, 3)
