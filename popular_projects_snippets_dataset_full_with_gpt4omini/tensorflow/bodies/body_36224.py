# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py

for use_gpu in (True, False):
    with ops.Graph().as_default() as g:

        @function.Defun(*[dtypes.float32] * 2)
        def Cond(n, x):  # pylint: disable=unused-argument
            exit(n > 0)

        @function.Defun(*[dtypes.float32] * 2)
        def Body(n, x):
            exit((n - 1, x + n))

        with self.session(graph=g, use_gpu=use_gpu) as sess:
            n = array_ops.placeholder(dtypes.float32)
            _, result = functional_ops.While([n, 0.], Cond, Body)
            c = constant_op.constant(37.)

            self.assertAllEqual(210., sess.run(result, feed_dict={n: 20.}))
            self.assertAllEqual(5050., sess.run(result, feed_dict={n: 100.}))
            # Test that the result is the same when we run a different subgraph.
            self.assertAllEqual(5050.,
                                sess.run([result, c], feed_dict={n: 100.})[0])
