# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
with self._delay_checks() as add_check:
    for padding in ["SAME", "VALID"]:
        for depth, height, width in [[9, 9, 10], [9, 10, 9]]:
            for kernel_depth, kernel_height, kernel_width in [[3, 3,
                                                               3], [3, 2, 2],
                                                              [2, 1, 3]]:
                for dilation_rate in [[1, 1, 1], [3, 3, 3], [3, 2, 3], [3, 1, 2]]:
                    self._test_atrous_convolution(
                        add_check=add_check,
                        input_shape=[2, depth, height, width, 2],
                        filter_shape=[
                            kernel_depth, kernel_height, kernel_width, 2, 2
                        ],
                        padding=padding,
                        dilation_rate=dilation_rate,
                    )
