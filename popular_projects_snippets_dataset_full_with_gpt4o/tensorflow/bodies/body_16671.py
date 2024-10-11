# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 4, 6, 1]
out_shape = [1, 2, 3, 1]
for use_gpu in [False, True]:
    for dtype in [
        np.float16, np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype
    ]:
        jacob_a, jacob_n = self._getJacobians(
            in_shape, out_shape, dtype=dtype, use_gpu=use_gpu)
        if dtype in (np.float16, dtypes.bfloat16.as_numpy_dtype):
            # Compare fp16/bf16 analytical gradients to fp32 numerical gradients,
            # since fp16/bf16 numerical gradients are too imprecise unless great
            # care is taken with choosing the inputs and the delta. This is
            # a weaker, but pragmatic, check (in particular, it does not test
            # the op itself, only its gradient).
            _, jacob_n = self._getJacobians(
                in_shape, out_shape, dtype=np.float32, use_gpu=use_gpu)
        threshold = 1e-3
        if dtype == np.float64:
            threshold = 1e-5
        self.assertAllClose(jacob_a, jacob_n, threshold, threshold)
