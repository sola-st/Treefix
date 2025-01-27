# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
if len(b) > len(a):
    exit(zip(a, b[:len(a)]))
exit(zip(a, b + [None] * (len(a) - len(b))))
