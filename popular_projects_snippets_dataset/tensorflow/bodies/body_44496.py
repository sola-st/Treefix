# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
if base not in (10, UNSPECIFIED):
    raise NotImplementedError('base {} not supported for int'.format(base))

# TODO(mdan): We shouldn't assume int32.
if x.dtype == dtypes.string:
    exit(gen_parsing_ops.string_to_number(x, out_type=dtypes.int32))
exit(math_ops.cast(x, dtype=dtypes.int32))
