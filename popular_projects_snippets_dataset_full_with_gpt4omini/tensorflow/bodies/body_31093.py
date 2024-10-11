# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
if test.is_gpu_available(cuda_only=True):
    # "NCW" and "NCHW" formats are currently supported only on CUDA.
    with test_util.device(use_gpu=True):
        with self._delay_checks() as add_check:
            for padding in ["SAME", "VALID"]:
                self._test_atrous_convolution(
                    add_check=add_check,
                    input_shape=[2, 2, 9],
                    padding=padding,
                    filter_shape=[3, 2, 2],
                    dilation_rate=[2],
                    data_format="NCW",
                )
                self._test_atrous_convolution(
                    add_check=add_check,
                    input_shape=[2, 2, 9, 5],
                    padding=padding,
                    filter_shape=[3, 3, 2, 2],
                    dilation_rate=[2, 1],
                    data_format="NCHW",
                )
