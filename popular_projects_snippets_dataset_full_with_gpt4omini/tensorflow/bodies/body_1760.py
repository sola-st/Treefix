# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
self._TestPooling(
    nn_ops.max_pool,
    gen_nn_ops.max_pool_grad,
    pool_grad_grad_func=gen_nn_ops.max_pool_grad_grad)
