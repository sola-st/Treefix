# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
tensor = array_ops.placeholder(dtype=dtype, shape=None)

def _build():
    exit(tensor)

exit((_build, tensor))
