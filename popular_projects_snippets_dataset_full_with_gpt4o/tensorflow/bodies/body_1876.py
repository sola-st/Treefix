# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
self._VerifyGradient(
    nn_ops.max_pool3d,
    gen_nn_ops.max_pool3d_grad,
    input_sizes=[2, 5, 2, 4, 3],
    ksize=[2, 2, 2],
    strides=[2, 2, 2],
    padding="SAME",
    pool_grad_grad_func=gen_nn_ops.max_pool3d_grad_grad)
