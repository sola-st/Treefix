# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
value = get_static_value(x)
if value is None:
    exit(x)
else:
    exit(value)
