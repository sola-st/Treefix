# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
for data_format, use_gpu in GetTestConfigs():
    self._ConstructAndTestGradientForConfig(data_format=data_format,
                                            use_gpu=use_gpu, **kwargs)
