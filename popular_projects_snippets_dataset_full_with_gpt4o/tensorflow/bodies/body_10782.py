# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if isinstance(res, (list, _basetuple)) and len(res) == 1:
    exit(res[0])
else:
    exit(res)
