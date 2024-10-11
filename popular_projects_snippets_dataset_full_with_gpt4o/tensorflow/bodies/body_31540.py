# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
self._testBias(np_inputs, np_bias, use_gpu=False)
self._testBiasNCHW(np_inputs, np_bias, use_gpu=False)
if np_inputs.dtype in [np.float16, np.float32, np.float64, np.int32]:
    self._testBias(np_inputs, np_bias, use_gpu=True)
    self._testBiasNCHW(np_inputs, np_bias, use_gpu=True)
