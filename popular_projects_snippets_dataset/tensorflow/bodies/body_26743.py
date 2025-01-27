# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
# x has leading dimension 5, this will raise an error
exit(array_ops.gather(x, 10))
