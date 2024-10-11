# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
for use_gpu in False, True:
    with self.cached_session(use_gpu=use_gpu):
        # Random values
        inp = np.asarray(np.random.rand(*input_shape))
        a = constant_op.constant(inp, dtype=dtypes.float64)
        tiled = array_ops.tile(a, multiples)
        grad_shape = list(np.array(multiples) * np.array(inp.shape))
        err = gradient_checker.compute_gradient_error(
            a, list(input_shape), tiled, grad_shape, x_init_value=inp)
    print("tile(float) error = ", err)
    self.assertLess(err, 1e-3)
