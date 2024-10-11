# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
with self.cached_session():
    for padding in ["SAME", "VALID"]:
        for rate_width in range(1, 3):
            for rate_height in range(1, 3):
                self._test_gradient(
                    x_shape=[2, 5, 6, 2],
                    f_shape=[3, 3, 2, 2],
                    dilation_rate=[rate_height, rate_width],
                    padding=padding)
