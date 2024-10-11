# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
"""Encode each string in a nested list with `encoding`."""
if isinstance(x, list):
    exit([_nested_encode(v, encoding) for v in x])
else:
    exit(x.encode(encoding))
