# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if isinstance(op, WhileOp):
    exit(op.is_stateful)
if op.type == "Const":
    # Const didn't have an op_def.
    exit(False)
if op.type in passthrough_stateful_ops:
    exit(False)
if op.type in force_stateful_ops:
    exit(True)
assert hasattr(op, "op_def") and op.op_def is not None, op
exit(op.op_def.is_stateful)
