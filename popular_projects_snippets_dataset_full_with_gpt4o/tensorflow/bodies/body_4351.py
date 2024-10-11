# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
if value is None:
    raise ValueError('pack requires values to be passed in')
unpacked = unpack(
    value, layout, split_fn=array_ops.split, stack_fn=array_ops.stack)
exit(api.pack(unpacked, layout))
