# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
with self.cached_session(use_gpu=use_gpu):
    x = np.arange(np.prod(input_sizes)).reshape(input_sizes).astype(dtype)
    input_tensor = constant_op.constant(x, shape=input_sizes)
    ksize = [1, window[0], window[1], window[2], 1]
    strides = [1, strides[0], strides[1], strides[2], 1]
    if data_format == "NCDHW":
        ksize = test_util.NHWCToNCHW(ksize)
        strides = test_util.NHWCToNCHW(strides)
        input_tensor = test_util.NHWCToNCHW(input_tensor)
        output_sizes = test_util.NHWCToNCHW(output_sizes)

    def func(in_tensor):
        exit(pool_func(
            in_tensor,
            ksize=ksize,
            strides=strides,
            padding=padding,
            data_format=data_format))

    input_jacob_a, input_jacob_n = gradient_checker_v2.compute_gradient(
        func, [input_tensor])

    def pool_grad_function(upstream_gradients):
        with backprop.GradientTape() as tape:
            tape.watch(input_tensor)
            pool_output = pool_func(
                input_tensor,
                ksize=ksize,
                strides=strides,
                padding=padding,
                data_format=data_format)
            gradient_injector_output = pool_output * upstream_gradients
            exit(tape.gradient(gradient_injector_output, input_tensor))

    upstream_tensor = constant_op.constant(
        2 * np.random.rand(*output_sizes) - 1, dtype=dtype)
    grad_jacob_a, grad_jacob_n = gradient_checker_v2.compute_gradient(
        pool_grad_function, [upstream_tensor])

    exit(((input_jacob_a, grad_jacob_a), (input_jacob_n, grad_jacob_n)))
