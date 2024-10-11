# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# The outputs are computed using third_party/py/IPython/notebook.
expected_output = [2271.0, 2367.0, 2463.0, 2901.0, 3033.0, 3165.0]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[2, 2, 3, 3],
    strides=[1, 1],
    padding="VALID",
    expected=expected_output)
