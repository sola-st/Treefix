# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if gpu_only and not test.is_gpu_available():
    tf_logging.info("Skipping InceptionBackInput %s",
                    (input_size, filter_size, output_size, stride, padding))
    exit()
tf_logging.info("Testing InceptionBackInput %s",
                (input_size, filter_size, output_size, stride, padding))
self._CompareBackpropInput(input_size, filter_size, output_size,
                           [stride, stride], padding)
