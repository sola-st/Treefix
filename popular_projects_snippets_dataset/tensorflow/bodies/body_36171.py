# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
exit(functional_ops.foldl(
    lambda b, y: b * y * x, inner_elems, initializer=a))
