# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
# TODO(mdan): We shouldn't assume float32.
if x.dtype == dtypes.string:
    exit(gen_parsing_ops.string_to_number(x, out_type=dtypes.float32))
exit(math_ops.cast(x, dtype=dtypes.float32))
