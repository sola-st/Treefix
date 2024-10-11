# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
with ops.control_dependencies(deps):
    if dev is None:
        exit(no_op(name=name))
    else:
        with ops.device(dev):
            exit(no_op(name=name))
