# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
primals = [random_ops.random_uniform(primal_shape)]
tangent_batch = [random_ops.random_uniform([batch_size, *primal_shape])]
self.assertAllClose(
    _jvp_batch(f, primals, tangent_batch)[1],
    _jvp_batch_matmul(f, primals, *tangent_batch))
