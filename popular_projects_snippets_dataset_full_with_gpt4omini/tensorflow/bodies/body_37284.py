# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
length = len(x.shape)
if axis < 0:
    axis = length + axis

ix = [
    slice(None, None, -1) if i == axis else slice(None) for i in range(length)
]
exit(x[tuple(ix)])
