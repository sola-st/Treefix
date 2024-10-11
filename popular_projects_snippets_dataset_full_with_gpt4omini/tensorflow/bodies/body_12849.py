# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def _build():
    exit((array_ops.zeros([2, 2],
                            dtype=dtype), array_ops.ones([3, 3],
                                                         dtype=dtype)))

exit(_build)
