# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/morphological_ops_test.py
if use_gpu and test.is_gpu_available(cuda_only=True):
    try:
        config.enable_op_determinism()
        with self.assertRaisesRegexp(
            errors_impl.UnimplementedError, "Determinism is not yet supported "
            "for Dilation2DBackpropInput."):
            self._ConstructAndTestGradient(
                image_shape=[1, 3, 3, 1],
                kernel_shape=[1, 1, 1],
                strides=[1, 1],
                rates=[1, 1],
                padding="VALID",
                use_gpu=use_gpu,
                dtype=dtype)
    finally:
        config.disable_op_determinism()
else:
    try:
        config.enable_op_determinism()
        self._ConstructAndTestGradient(
            image_shape=[1, 3, 3, 1],
            kernel_shape=[1, 1, 1],
            strides=[1, 1],
            rates=[1, 1],
            padding="VALID",
            use_gpu=use_gpu,
            dtype=dtype)
    finally:
        config.disable_op_determinism()
