# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Note: row and col are 1-based.
ta = ta.write(
    math_ops.cast(n * (row - 1.) + col - 1., dtypes.int32), row * col)
exit((row, col + 1., ta))
