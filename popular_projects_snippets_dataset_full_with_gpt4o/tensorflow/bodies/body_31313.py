# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pool_test.py
with self.session(use_gpu=test.is_gpu_available()):
    for padding in ["SAME", "VALID"]:
        for pooling_type in ["MAX", "AVG"]:
            for input_shape in [[2, 9, 2], [2, 10, 2]]:
                for window_shape in [[1], [2], [3]]:
                    if padding != "SAME":
                        for dilation_rate in [[1], [2], [3]]:
                            self._test(
                                input_shape=input_shape,
                                window_shape=window_shape,
                                padding=padding,
                                pooling_type=pooling_type,
                                dilation_rate=dilation_rate,
                                strides=[1])
                    for strides in [[1], [2], [3]]:
                        if np.any(np.array(strides) > window_shape):
                            continue
                        self._test(
                            input_shape=input_shape,
                            window_shape=window_shape,
                            padding=padding,
                            pooling_type=pooling_type,
                            dilation_rate=[1],
                            strides=strides)
