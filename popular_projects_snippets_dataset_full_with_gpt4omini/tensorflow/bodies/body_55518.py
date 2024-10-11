# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# Cannot rely on `nest` because the leaves are tuples.
if not isinstance(values, (list, tuple)):
    _check_failed(values)
if isinstance(values, tuple):
    _ = [_check_int(v) for v in values]
else:
    _ = [_check_quantized(v) for v in values]
