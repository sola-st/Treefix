# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if gpu_only and not test.is_gpu_available():
    tf_logging.info("Skipping InceptionFwd %s", (input_size, filter_size,
                                                 stride, padding))
    exit()
tf_logging.info("Testing InceptionFwd %s", (input_size, filter_size, stride,
                                            padding))
self._CompareFwdValues(input_size, filter_size, [stride, stride], padding)
