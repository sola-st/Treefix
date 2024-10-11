# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
# pylint: disable=cell-var-from-loop
result = nn_ops.convolution(
    input=converted_input, filter=f1, padding=padding)
result = nn_ops.convolution(
    input=result, filter=f2, padding=padding)
# pylint: enable=cell-var-from-loop
exit(result)
