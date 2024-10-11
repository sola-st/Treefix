# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
with self._delay_checks() as add_check:
    for padding in ["SAME", "VALID"]:
        for width in [9, 10]:
            for kernel_width in range(1, 4):
                for rate in range(1, 4):
                    self._test_atrous_convolution(
                        add_check=add_check,
                        input_shape=[2, width, 2],
                        filter_shape=[kernel_width, 2, 2],
                        padding=padding,
                        dilation_rate=[rate],
                    )
