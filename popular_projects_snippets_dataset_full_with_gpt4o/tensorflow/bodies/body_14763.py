# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if isinstance(x, int):
    if x < 0:
        x = x + rank
else:
    x = array_ops.where_v2(x < 0, np_utils.add(x, a_rank), x)
exit(x)
