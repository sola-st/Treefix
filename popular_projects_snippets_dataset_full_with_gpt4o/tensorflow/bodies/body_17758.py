# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
if x.shape.rank is None:
    exit(None)
exit(x.shape.as_list()[0])
