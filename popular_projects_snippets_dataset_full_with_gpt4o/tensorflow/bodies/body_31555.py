# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
with self.cached_session(use_gpu=use_gpu):
    if data_format == "NCHW":
        np_input = self._NHWCToNCHW(np_input)
    jacob_a, jacob_n = self._computeGradient(np_input, bias, dtype,
                                             data_format)
    input_jacob_a, bias_jacob_a, grad_jacob_a = jacob_a
    input_jacob_n, bias_jacob_n, grad_jacob_n = jacob_n

    if dtype in [np.float16, dtypes.bfloat16.as_numpy_dtype]:
        # Compare fp16/bf16 analytical gradients to fp32 numerical gradients,
        # since fp16/bf16 numerical gradients are too imprecise unless great
        # care is taken with choosing the inputs and the delta. This is
        # a weaker, but pragmatic, check (in particular, it does not test
        # the op itself, only its gradient).
        _, jacob_n = self._computeGradient(np_input, bias, np.float32,
                                           data_format)
        input_jacob_n, bias_jacob_n, grad_jacob_n = jacob_n

    if dtype == dtypes.float64:
        threshold = 1e-10
    elif np_input.size >= 512:
        # The 5e-3 threshold seems to have been marginal in these cases, and
        # small changes in the test were pushing it over the limit.
        threshold = 5e-2
    else:
        threshold = 5e-3
    self.assertAllClose(input_jacob_a, input_jacob_n, threshold, threshold)
    self.assertAllClose(bias_jacob_a, bias_jacob_n, threshold, threshold)
    self.assertAllClose(grad_jacob_a, grad_jacob_n, threshold, threshold)
