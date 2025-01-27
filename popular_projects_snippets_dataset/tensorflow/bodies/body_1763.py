# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
self._VerifyValues(
    nn_ops.max_pool,
    gen_nn_ops.max_pool_grad,
    input_sizes=[1, 7, 7, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 3, 3, 1],
    padding="VALID")
