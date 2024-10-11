# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
with ops.control_dependencies([check_ops.assert_equal(x, 0)]):
    exit(array_ops.identity(x))
