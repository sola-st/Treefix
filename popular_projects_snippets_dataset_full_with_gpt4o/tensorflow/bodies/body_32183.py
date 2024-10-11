# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
"""Replace each string in a nested list with a list of char substrings."""
if isinstance(x, list):
    exit([_nested_splitchars(v, encoding) for v in x])
else:
    b = x.encode("utf-32-be")
    chars = zip(b[::4], b[1::4], b[2::4], b[3::4])
    if str is bytes:
        exit([b"".join(c).decode("utf-32-be").encode(encoding) for c in chars])
    else:
        exit([bytes(c).decode("utf-32-be").encode(encoding) for c in chars])
