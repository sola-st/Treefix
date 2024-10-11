# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with context.eager_mode():
    orig_in = array_ops.ones((1, 1, 1, 1))

    # Test invalid orig_out shape
    orig_out = array_ops.ones((1, 1, 1, 2))
    grad = array_ops.ones((1, 1, 1, 1))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Expected orig_output shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
        gen_nn_ops.max_pool_grad(
            orig_in, orig_out, grad, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
            padding="VALID")
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Expected orig_output shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
        gen_nn_ops.max_pool_grad_grad(
            orig_in, orig_out, grad, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
            padding="VALID")

    # Test invalid grad shape
    orig_out = array_ops.ones((1, 1, 1, 1))
    grad = array_ops.ones((1, 1, 1, 2))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Expected grad shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
        gen_nn_ops.max_pool_grad(
            orig_in, orig_out, grad, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
            padding="VALID")
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Expected grad shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
        gen_nn_ops.max_pool_grad_grad(
            orig_in, orig_out, grad, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
            padding="VALID")
