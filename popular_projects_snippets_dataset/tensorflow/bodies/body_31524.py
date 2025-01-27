# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py

def Test(self):
    if gpu_only and not test.is_gpu_available():
        tf_logging.info("Skipping InceptionBackFilter %s",
                        (input_size, filter_size, output_size, strides, padding))
        exit()
    tf_logging.info("Testing InceptionBackFilter %s",
                    (input_size, filter_size, output_size, strides, padding))
    self._CompareBackFilter(input_size, filter_size, output_size, strides,
                            padding)

exit(Test)
