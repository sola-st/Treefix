# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
with self._delay_checks() as add_check:
    for padding in ["SAME", "VALID"]:
        for height, width in [[9, 9], [9, 10]]:
            for kernel_height, kernel_width in [[1, 1], [2, 2], [2, 3]]:
                for dilation_rate in [[1, 1], [3, 2], [2, 1]]:
                    self._test_atrous_convolution(
                        add_check=add_check,
                        input_shape=[2, height, width, 2],
                        filter_shape=[kernel_height, kernel_width, 2, 2],
                        padding=padding,
                        dilation_rate=dilation_rate,
                    )
