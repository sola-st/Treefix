# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with context.eager_mode():
    inp = array_ops.ones((1, 1, 1, 1))

    # Test invalid grad shape
    grad = array_ops.ones((1, 1, 1, 2))
    argmax = array_ops.zeros((1, 1, 1, 1), dtype=dtypes.int64)
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Expected grad shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
        gen_nn_ops.max_pool_grad_with_argmax(
            inp, grad, argmax, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
            padding="VALID")
    # max_pool_grad_grad_with_argmax is only implemented for GPUs
    if test.is_gpu_available():
        with self.assertRaisesRegex(
            errors_impl.InvalidArgumentError,
            r"Expected grad shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
            gen_nn_ops.max_pool_grad_grad_with_argmax(
                inp, grad, argmax, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
                padding="VALID")

      # Test invalid argmax shape
    grad = array_ops.ones((1, 1, 1, 1))
    argmax = array_ops.ones((1, 1, 1, 2), dtype=dtypes.int64)
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Expected argmax shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
        gen_nn_ops.max_pool_grad_with_argmax(
            inp, grad, argmax, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
            padding="VALID")
    # max_pool_grad_grad_with_argmax is only implemented for GPUs
    if test.is_gpu_available():
        with self.assertRaisesRegex(
            errors_impl.InvalidArgumentError,
            r"Expected argmax shape to be \[1,1,1,1\], but got \[1,1,1,2\]"):
            gen_nn_ops.max_pool_grad_grad_with_argmax(
                inp, grad, argmax, ksize=[1, 1, 1, 1], strides=[1, 1, 1, 1],
                padding="VALID")
