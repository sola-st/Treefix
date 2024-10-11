# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
assert value is not None
unpacked = unpack(value, layout)
if make_sparse:
    exit(api.pack([sparse_ops.from_dense(t) for t in unpacked], layout))
exit(api.pack(unpacked, layout))
