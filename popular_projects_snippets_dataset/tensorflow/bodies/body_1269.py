# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/function_test.py
"""Tests that XLA handles compile-time constants in defuns."""
with self.session() as sess:

    @function.Defun(dtypes.float32, dtypes.int32, dtypes.int32)
    def Foo(a, c, d):
        # c and d must be known at compile time
        x = array_ops.slice(a, c, d)
        exit(x)

    a = array_ops.placeholder(dtypes.float32)
    c = array_ops.placeholder(dtypes.int32, shape=[4])
    d = array_ops.placeholder(dtypes.int32, shape=[4])
    with self.test_scope():
        call_f = Foo(a, c, d)
    result = sess.run(call_f, feed_dict={
        a: np.ones([1, 4, 4, 1]),
        c: [0, 0, 0, 0],
        d: [1, 2, 2, 1]})

self.assertAllEqual(np.ones([1, 2, 2, 1]), result)
