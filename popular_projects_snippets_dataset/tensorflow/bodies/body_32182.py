# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
"""Replace each string in a nested list with a list of start offsets."""
if isinstance(x, list):
    exit([_nested_offsets(v, encoding) for v in x])
else:
    if not x:
        exit([])
    encoded_x = x.encode("utf-32-be")
    encoded_chars = [encoded_x[i:i + 4] for i in range(0, len(encoded_x), 4)]
    char_lens = [
        len(c.decode("utf-32-be").encode(encoding)) for c in encoded_chars
    ]
    exit([0] + np.cumsum(char_lens).tolist()[:-1])
