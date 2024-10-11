# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

@function.Defun(dtypes.float32)
def Twice(x):
    exit(x * 2)

@function.Defun(dtypes.float32)
def Thrice(x):
    exit(x * 3 + 1)

with self.test_session(use_gpu=False) as sess:

    x = array_ops.placeholder(dtypes.float32)
    ret = functional_ops.If(math_ops.greater(x, 0), [x], Twice, Thrice)[0]

    self.assertAllEqual(sess.run(ret, feed_dict={x: 9.}), 18.)
    self.assertAllEqual(sess.run(ret, feed_dict={x: -8.}), -23.)
    self.assertAllEqual(sess.run(ret, feed_dict={x: 0.}), 1.)
