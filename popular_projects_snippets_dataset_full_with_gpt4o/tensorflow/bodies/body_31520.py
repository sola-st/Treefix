# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py

def Test(self):
    if stride == 1:
        tf_logging.info("Testing InceptionFwd with dilations %s",
                        (input_size, filter_size, stride, padding))
        self._VerifyDilatedConvValues(
            tensor_in_sizes=input_size,
            filter_in_sizes=filter_size,
            strides=[stride, stride],
            dilations=[2, 2],
            padding=padding,
            rtol=5e-4)

exit(Test)
