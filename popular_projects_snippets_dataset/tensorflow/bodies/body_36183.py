# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtype=dtypes.float32, shape=[None, 2])
    x_t = array_ops.transpose(x)
    # scan over dimension 0 (with shape None)
    result = functional_ops.scan(lambda a, x: a + x, x)
    # scanned over transposed dimension 0 (with shape 2)
    result_t = functional_ops.scan(lambda a, x: a + x, x_t, infer_shape=False)
    # ensure gradients can be calculated
    result_grad = gradients_impl.gradients(result, [x])[0]
    result_t_grad = gradients_impl.gradients(result_t, [x_t])[0]

    # smoke test to ensure they all evaluate
    sess.run([result, result_t, result_grad, result_t_grad],
             feed_dict={x: [[1.0, 2.0]]})
