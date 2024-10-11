# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
if test.is_gpu_available(cuda_only=True):
    # "NC*" format is currently only supported on CUDA.
    with self.session():
        for padding in ["SAME", "VALID"]:
            self._test(
                input_shape=[2, 2, 9],
                window_shape=[2],
                padding=padding,
                pooling_type="MAX",
                strides=[1],
                dilation_rate=[1],
                data_format="NCW")
            self._test(
                input_shape=[2, 2, 9],
                window_shape=[2],
                padding=padding,
                pooling_type="MAX",
                strides=[2],
                dilation_rate=[1],
                data_format="NCW")
            self._test(
                input_shape=[2, 2, 7, 9],
                window_shape=[2, 2],
                padding=padding,
                pooling_type="MAX",
                strides=[1, 2],
                dilation_rate=[1, 1],
                data_format="NCHW")
            self._test(
                input_shape=[2, 2, 7, 5, 3],
                window_shape=[2, 2, 2],
                padding=padding,
                pooling_type="MAX",
                strides=[1, 2, 1],
                dilation_rate=[1, 1, 1],
                data_format="NCDHW")
        self._test(
            input_shape=[2, 2, 7, 9],
            window_shape=[2, 2],
            padding="VALID",
            pooling_type="MAX",
            strides=[1, 1],
            dilation_rate=[2, 2],
            data_format="NCHW")
