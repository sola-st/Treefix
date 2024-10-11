# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
list_of_stuff = [
    constant_op.constant([11, 22]), constant_op.constant([1, 2])
]
check_ops.assert_proper_iterable(list_of_stuff)
