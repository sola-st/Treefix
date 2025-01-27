# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
# VALID padding
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 3, 3, 3],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="VALID",
    pool_grad_grad_func=pool_grad_grad_func)

# SAME padding
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 2, 3, 3],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    pool_grad_grad_func=pool_grad_grad_func)

# SAME padding, non square window
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 2, 2, 1],
    ksize=[1, 1, 2, 1],
    strides=[1, 1, 1, 1],
    padding="SAME",
    pool_grad_grad_func=pool_grad_grad_func)

# VALID padding, uneven stride
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 4, 4, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 1, 2, 1],
    padding="VALID",
    pool_grad_grad_func=pool_grad_grad_func)
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 4, 4, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 1, 1],
    padding="VALID",
    pool_grad_grad_func=pool_grad_grad_func)

# SAME padding, size 4 input
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 4, 4, 4],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    pool_grad_grad_func=pool_grad_grad_func)

# SAME padding, size 8 input
self._VerifyValues(
    forward_op,
    backward_op,
    input_sizes=[1, 8, 8, 8],
    ksize=[1, 3, 3, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    pool_grad_grad_func=pool_grad_grad_func)
