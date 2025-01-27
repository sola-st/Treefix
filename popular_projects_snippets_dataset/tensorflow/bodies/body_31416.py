# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if test.is_gpu_available(cuda_only=True) or test_util.IsMklEnabled():
    data_formats = ["NHWC", "NCHW"]
else:
    data_formats = ["NHWC"]
for data_format in data_formats:
    for dilation in [1, 2]:
        for stride in [1, 2]:
            for filter_dims in [[3, 3, 4, 8], [1, 1, 2, 16]]:
                self._VerifyGroupConvFwd([10, 32, 32, 16], filter_dims,
                                         dilations=[dilation, dilation],
                                         strides=[stride, stride],
                                         padding="SAME",
                                         data_format=data_format,
                                         dtype=dtypes.float32)
