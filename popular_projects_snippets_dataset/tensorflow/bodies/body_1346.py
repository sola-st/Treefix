# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
# pylint: disable=unnecessary-lambda
exit(functional_ops.scan(
    lambda a, x: math_ops.multiply(a, x), y, initializer=v))
