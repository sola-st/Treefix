# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Sets gradient "grad" in "grads" for tensor "t"."""
op = t.op
op_grads = grads.get(op)
if not op_grads:
    op_grads = [[] for _ in range(len(op.outputs))]
    grads[op] = op_grads
t_grads = op_grads[t.value_index]
if isinstance(t_grads, list):
    t_grads.append(grad)
else:
    assert control_flow_util.IsLoopSwitch(op)
    op_grads[t.value_index] = grad
