# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
with self.session(use_gpu=test.is_gpu_available()):
    for padding in ["SAME", "VALID"]:
        for pooling_type in ["MAX", "AVG"]:
            self._test(
                input_shape=[1, 1, 10, 1],
                window_shape=[1, 3],
                padding=padding,
                pooling_type=pooling_type,
                dilation_rate=[1, 1],
                strides=[1, 2])
