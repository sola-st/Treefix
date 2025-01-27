# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
with self.session() as sess:
    inputs = array_ops.placeholder(dtypes.float32, shape=[2, 5])
    values, _ = nn_ops.top_k(inputs, 3)
    grad = sess.run(
        gradients_impl.gradients(
            values, inputs, grad_ys=[[[1., 2., 3.], [4., 5., 6.]]]),
        feed_dict={inputs: [[2., -1., 1000., 3., 4.],
                            [1., 5., 2., 4., 3.]]})[0]
self.assertEqual(
    grad.tolist(), [[0., 0., 1., 3., 2.], [0., 4., 0., 5., 6.]])
