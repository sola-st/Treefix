# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
# TODO(b/73062247): the bfloat16 implementation of MaxPool3DGradGrad does
# not have enough precision for this test case to pass if
# pool_grad_grad_func is passed.
self._VerifyGradient(
    nn_ops.max_pool3d,
    gen_nn_ops.max_pool3d_grad,
    input_sizes=[2, 3, 5, 7, 3],
    ksize=[2, 2, 2],
    strides=[1, 1, 1],
    padding="VALID")
