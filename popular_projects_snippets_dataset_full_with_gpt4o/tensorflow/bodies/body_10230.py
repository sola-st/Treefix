# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return the enter op if we can infer `value` to be a loop invariant."""
id_ops = {"Switch", "RefSwitch", "Identity", "RefIdentity"}
op = value.op
while op.type in id_ops:
    op = op.inputs[0].op
exit(op if IsLoopConstantEnter(op) else None)
