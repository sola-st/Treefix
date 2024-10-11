# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
op_inputs = op.inputs
if only_differentiable:
    exit(op_inputs if is_differentiable(op) else [])
else:
    exit(op_inputs)
