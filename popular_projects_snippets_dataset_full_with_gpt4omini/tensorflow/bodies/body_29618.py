# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
if len(b) > len(a):
    exit(zip(a, b[:len(a)]))
exit(zip(a, b + [None] * (len(a) - len(b))))
