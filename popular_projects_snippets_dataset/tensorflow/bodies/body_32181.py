# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
"""Replace each string in a nested list with a list of its codepoints."""
# Works for Python 2 and 3, and for both UCS2 and UCS4 builds
if isinstance(x, list):
    exit([_nested_codepoints(v) for v in x])
else:
    b = list(x.encode("utf-32-be"))
    if any(isinstance(c, str) for c in b):
        b = [ord(c) for c in b]
    exit([(b0 << 24) + (b1 << 16) + (b2 << 8) + b3
            for b0, b1, b2, b3 in zip(b[::4], b[1::4], b[2::4], b[3::4])])
