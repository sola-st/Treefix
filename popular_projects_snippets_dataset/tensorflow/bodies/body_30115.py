# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with context.eager_mode():
    v = variables.Variable([1., 2.])
    v[0]  # pylint: disable=pointless-statement
