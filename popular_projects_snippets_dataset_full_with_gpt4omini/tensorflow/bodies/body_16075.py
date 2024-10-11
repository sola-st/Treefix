# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_op_test.py
if isinstance(x, list):
    exit([self._str_to_bytes(v) for v in x])
elif isinstance(x, str) and bytes is not str:
    exit(bytes(x, 'utf-8'))
else:
    exit(x)
