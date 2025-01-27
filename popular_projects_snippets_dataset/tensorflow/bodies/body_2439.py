# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
spec = [
    _slice(start, limit, stride)
    for (start, limit, stride) in zip(start_dims, limit_dims, strides)
]
exit(x[tuple(spec)])
