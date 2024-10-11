# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
# The outputs are computed using third_party/py/IPython/notebook.
# With a shift of 21, we should execute the optimized path here.
expected_output = [
    231.0, 252.0, 273.0, 384.0, 423.0, 462.0, 690.0, 765.0, 840.0, 843.0,
    936.0, 1029.0
]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[1, 2, 3, 3],
    stride=1,
    padding="VALID",
    expected=expected_output)
