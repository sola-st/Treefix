# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for data_format in ("NCHW", "NHWC"):
    for stacked_value in (True, False):
        x_shape = [3, 4, 5, 6]
        if stacked_value:
            x_shape = [2] + x_shape
        x = random_ops.random_uniform(x_shape)
        for stacked_bias in (True, False):
            if not (stacked_value or stacked_bias):
                continue
            with backprop.GradientTape(persistent=True) as g:
                bias_dim = -1
                if data_format == "NCHW":
                    bias_dim = 2 if stacked_value else 1
                bias_shape = [x_shape[bias_dim]]
                if stacked_bias:
                    bias_shape = [2] + bias_shape
                bias = random_ops.random_uniform(bias_shape)
                g.watch(bias)

            # pylint: disable=cell-var-from-loop
            def loop_fn(i):
                with g:
                    a = array_ops.gather(x, i) if stacked_value else x
                    b = array_ops.gather(bias, i) if stacked_bias else bias
                    y = nn.bias_add(a, b, data_format=data_format)
                    loss = math_ops.reduce_sum(y * y)
                grad = g.gradient(loss, bias)
                if stacked_bias:
                    # If we gather over bias in loop_fn, the gradient will be an
                    # instance of `IndexedSlices` with attrs `values` and `indices`.
                    exit((y, grad.values, grad.indices))
                else:
                    exit((y, grad))

          # pylint: enable=cell-var-from-loop

            out_dtypes = [dtypes.float32, dtypes.float32]
            if stacked_bias:
                out_dtypes = out_dtypes + [dtypes.int32]
            self._test_loop_fn(loop_fn, 2)
