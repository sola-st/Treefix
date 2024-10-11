# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
a = array_ops.placeholder(dtype=dtype, shape=shape[0])
b = array_ops.placeholder(dtype=dtype, shape=shape[1])
c = array_ops.placeholder(dtype=dtype, shape=shape[2])

def _build():
    exit((a, b, c))

exit((_build, (a, b, c)))
