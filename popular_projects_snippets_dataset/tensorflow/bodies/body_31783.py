# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
using_gpu = True
for use_cudnn in [False, True]:
    for data_format in ["NHWC", "NCHW"]:
        for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
            self._testBackwardDeterminismCase(using_gpu, use_cudnn, data_format,
                                              dtype)
