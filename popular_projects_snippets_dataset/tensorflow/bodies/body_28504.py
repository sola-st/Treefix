# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
with ops.control_dependencies([check_ops.assert_equal(x, 0)]):
    exit(x)
