# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
"""Converts the inner list elements to strings."""
if isinstance(values, list):
    exit([_to_str_elements(value) for value in values])
else:
    exit(str(values).encode("utf-8"))
